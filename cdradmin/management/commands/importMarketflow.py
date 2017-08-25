import logging
from ._mfManager import MfManager
from ...models import Liability
from ...models import Superid
from ...models import loan

# https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
from django.core.management.base import BaseCommand

#import progressbar



class Command(BaseCommand):
  help = """Usage:
         python manage.py importMarketflow --help
         python manage.py importMarketflow --debug
         """

  def add_arguments(self, parser):
    parser.add_argument('--debug', action='store_true', dest='debug', default=False, help='show higher verbosity')

  def handle(self, *args, **options):
    h1 = logging.StreamHandler(stream=self.stderr)
    logger.addHandler(h1)
    if options['debug']:
      logger.setLevel(logging.DEBUG)

    with MfManager() as mfMan:
  
      total = mfMan.superidsCount()
      logger.debug("Django import superids: %s"%total)
      if options['debug']:
        counter = 0
        progress = progressbar.ProgressBar(maxval=total).start()
      for superidMf in mfMan.superidsList():
        if options['debug']:
          counter+=1
          if counter % 100 == 0:
            progress.update(counter)
  
        # get/create entity/row/case
        superidDj = Superid.objects.filter(
          superid_symbol=superidMf['CLI_SUPERID']
        ).first()
        if superidDj is None:
          superidDj = Superid.objects.create(
            superid_symbol=superidMf['CLI_SUPERID'],
            superid_name=superidMf['CLI_NOM_PRE'],
          )
          logger.debug("Created superid: %s"%superidDj)
        else:
          if superidDj.superid_name!=superidMf['CLI_NOM_PRE']:
            superidDj.superid_name=superidMf['CLI_NOM_PRE']
            superidDj.save()
            logger.debug("Updated superid: %s"%superidDj)

      if options['debug']:
        progress.finish()
