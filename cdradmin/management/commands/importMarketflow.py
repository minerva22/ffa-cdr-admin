import logging
from ._mfManager import MfManager
from ...models import Liability
from ...models import Superid
from ...models import Loan

# https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
from django.core.management.base import BaseCommand

import progressbar
logger = logging.getLogger('FFA Cdr admin')


class Command(BaseCommand):
  help = """Usage:
         python manage.py importMarketflow --help
         python manage.py importMarketflow --debug
         """

  def add_arguments(self, parser):
    parser.add_argument('--debug', action='store_true', dest='debug', default=False, help='show higher verbosity')
    parser.add_argument('--host',    action='store',      dest='host',  required=True, help='ms sql server for marketflow: host IP or name')
    parser.add_argument('--port',    action='store',      dest='port',  required=True, help='ms sql server for marketflow: port number')
    parser.add_argument('--user',    action='store',      dest='user',  required=True, help='ms sql server for marketflow: username')
    parser.add_argument('--password',action='store',  dest='password',  required=True, help='ms sql server for marketflow: password')
    parser.add_argument('--db',      action='store',      dest='db',    required=True, help='ms sql server for marketflow: database name')

  def handle(self, *args, **options):
    h1 = logging.StreamHandler(stream=self.stderr)
    logger.addHandler(h1)
    if options['debug']:
      logger.setLevel(logging.DEBUG)

    with MfManager(host=options['host'], port=options['port'], user=options['user'], password=options['password'], db=options['db']) as mfMan:
  
      total = mfMan.superidsCount()
      logger.debug("Django import superids: %s"%total)
      if options['debug']:
        counter = 0
        progress = progressbar.ProgressBar(maxval=total).start()
      for superidMf in mfMan.superidsList():
        if options['debug']:
          counter+=1
          if counter % 100 == 0:
            # logger.debug("%s / %s"%(counter,total))
            progress.update(counter)
  
        # get/create entity/row/case
        superidDj, created = Superid.objects.update_or_create(
          superid=superidMf['CLI_SUPERID'],
          defaults={
            'name': superidMf['Main_Holder_Name'],
          }
        )
        if created:
          if options['debug']:
            logger.debug("Created superid %s / %s: %s"%(counter, total, superidDj))

      if options['debug']:
        progress.finish()
