import logging
from ._mfManager import MfManager
from ...models import Liability
from ...models import Superid
from ...models import Loan
from ...models import Country
from ...models import Currency

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
    #parser.add_argument('--origin', action='store', dest='origin',required=True, help='set origin')
    parser.add_argument('--host',    action='store',      dest='host',  required=True, help='ms sql server for marketflow: host IP or name')
    parser.add_argument('--port',    action='store',      dest='port',  required=True, help='ms sql server for marketflow: port number')
    parser.add_argument('--user',    action='store',      dest='user',  required=True, help='ms sql server for marketflow: username')
    parser.add_argument('--password',action='store',  dest='password',  required=True, help='ms sql server for marketflow: password')
    parser.add_argument('--db',      action='store',      dest='db',    required=True, help='ms sql server for marketflow: database name')

  def _handle_superid(self, mfMan, options):
   
   total=mfMan.superidsCount()
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
            logger.debug("Created superid %s / %s: %s"%(counter, total, superidDj))

   if options['debug']:
      progress.finish()


  def _handle_country(self, mfMan, options):

   total=mfMan.countryCount()
   logger.debug("Django import countries: %s"%total)
      
   if options['debug']:
      counter = 0
      progress = progressbar.ProgressBar(maxval=total).start()

   for countryMf in mfMan.countryList():
     if options['debug']:
        counter+=1
        if counter % 100 == 0:
            # logger.debug("%s / %s"%(counter,total))
            progress.update(counter)
  
       # get/create entity/row/case
       
        countryDj, created = Country.objects.update_or_create(
         # name=countryMf['Ctry_Desc1'],
          defaults={
            'name': countryMf['Ctry_Desc1'],
          }
        )
        if created:
            logger.debug("Created country %s / %s: %s"%(counter, total, countryDj))

   if options['debug']:
      progress.finish()





  def _handle_currency(self, mfMan, options):

   total=mfMan.currencyCount()
   logger.debug("Django import currencies: %s"%total)

   if options['debug']:
      counter = 0
      progress = progressbar.ProgressBar(maxval=total).start()

   for currencyMf in mfMan.currencyList():
     if options['debug']:
        counter+=1
        if counter % 100 == 0:
            # logger.debug("%s / %s"%(counter,total))
            progress.update(counter)

       # get/create entity/row/case

        currencyDj, created = Currency.objects.update_or_create(
          #name=countryMf['Ctry_Desc1'],
          defaults={
            'name': currencyMf['DEV_SYM_LGE1'],
          }
        )
        if created:
            logger.debug("Created currency %s / %s: %s"%(counter, total, currencyDj))

   if options['debug']:
      progress.finish()


  def handle(self, *args, **options):
    h1 = logging.StreamHandler(stream=self.stderr)
    logger.addHandler(h1)
    if options['debug']:
      logger.setLevel(logging.DEBUG)

    with MfManager(host=options['host'], port=options['port'], user=options['user'], password=options['password'], db=options['db']) as mfMan:  
     # self._handle_superid(mfMan, options)
      #self._handle_country(mfMan, options)
     # self._handle_currency(mfMan, options)
