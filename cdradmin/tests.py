from django.test import TestCase
from cdradmin.models import Currency,Loan,Liability,Superid,Country,Ledger,SuperidToLoanLiability


# Create your tests here.

class CurrencyTestCase(TestCase):


    def test_currency(self):
       currency1 = Currency.objects.create(code='00',name='test', description='desc')
       currency2 = Currency.objects.create(code='01',name='test2', description='desc')

#       actual = currency1.__str__()
       
       
       self.assertEqual(currency1.name, 'test')
       self.assertEqual(currency2.code,'01')

    
    def test_loan(self):
        loan1= Loan.objects.create(short_description='z22', long_description='cest un test')

        self.assertEqual(loan1.short_description, 'z22')

    def test_liability(self):
        liability1= Liability.objects.create(short_description='AV22', long_description='cest un test')

        self.assertEqual(liability1.short_description, 'AV22')

    def test_superid(self):
        superid1= Superid.objects.create(superid='2222', name='viva')
        self.assertEqual(superid1.superid,'2222')

    def test_country(self):
         country1= Country.objects.create(country='1',name='test')
         self.assertEqual(country1.country,'1')

            
    def test_ledger(self):
        ledger1= Ledger.objects.create(ledger='001',name='test')
        self.assertEqual(ledger1.ledger,'001')

    def test_SuperidToLoanLiability(self):

        Sup=SuperidToLoanLiability(
        Superid.objects.create(superid='22222', name='vivaa'),
        Loan.objects.create(short_description='z222', long_description='cesttt un test'),
        Liability.objects.create(short_description='AVV22', long_description='cest un testtt'),
        Ledger.objects.create(ledger='0001',name='testt'),
        Country.objects.create(country='00',name='testt'),
        Currency.objects.create(code='000',name='tett',description='testtt'),
        closed= '1',
        guarantee='0',
        maturity_date='',

        )
       
        self.assertEqual(Sup.closed,'1')
