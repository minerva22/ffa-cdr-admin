from __future__ import unicode_literals

from django.db import models


class Loan(models.Model):


     short_description = models.CharField(max_length=255)
     long_description = models.CharField(max_length=600)


     def __str__(self):
        return "%s: %s" %(self.short_description, self.long_description)

class Liability(models.Model):
    
      short_description = models.CharField(max_length=255)
      long_description = models.CharField(max_length=600)

      def __str__(self):
        return "%s: %s" %(self.short_description, self.long_description)


class Superid(models.Model):
     
     superid = models.IntegerField(default=0)
     name = models.CharField(max_length=255)
   
     
     
     def __str__(self):
        #return str(self.superid)+": "+self.name
        return "%s: %s"%(self.superid, self.name) 
     
class SuperidToLoanLiability(models.Model):
     
     superid = models.ForeignKey(Superid)
     loan = models.ForeignKey(Loan)
     liability = models.ForeignKey(Liability)
     maturity_date = models.DateField()
     country_of_utilization = models.CharField(max_length=255)
     ledger =  models.CharField(max_length=255)
     
     def __str__(self):
        return "%s: %s, %s, %s, %s, %s"%(self.superid, self.loan, self.liability, self.maturity_date, self.country_of_utilization,self.ledger)



