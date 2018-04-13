from django.test import TestCase
from cdradmin.models import Currency,Loan,Liability,Superid,Country,Ledger,SuperidToLoanLiability
from django.urls import reverse

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

        def test_asjson(self):
             url = reverse('cdradmin:index')
             response = self.client.get(url)
             self.assertEqual(response.status_code, 200)



from django.core.exceptions import ValidationError

class SuperidToLoanLiabilityModelTest(TestCase):
    def test_currency_different_than_guarantee_for(self):
      superid = Superid.objects.create(superid='22222', name='vivaa')
      loan_type = Loan.objects.create(short_description='z222', long_description='cesttt un test')
      ledger = Ledger.objects.create(ledger='0001',name='testt')
      country = Country.objects.create(cdr_code='00',name='testt')
      c_ash = Currency.objects.create(code=13,name='LBP',description='testtt')
      c_tbi = Currency.objects.create(code=2, name='USD',description='testtt')
      l_ash = Liability.objects.create(short_description='ASH', long_description='cest un testtt')
      l_tbi = Liability.objects.create(short_description='TBI', long_description='cest un testtt')

      s_ash=SuperidToLoanLiability.objects.create(
        superid = superid,
        loan_type = loan_type,
        liability_type = l_ash,
        guarantee_for = None,
        ledger = ledger,
        country_of_utilization = country,
        currency_liability = c_ash,
        closed= False
      )

      s_tbi=SuperidToLoanLiability.objects.create(
        superid = superid,
        loan_type = loan_type,
        liability_type = l_tbi,
        guarantee_for = s_ash,
        ledger = None,
        country_of_utilization = country,
        currency_liability = c_tbi,
        closed= False
      )
      with self.assertRaises(ValidationError):
        s_tbi.full_clean()

