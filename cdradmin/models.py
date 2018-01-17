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
   
     class Meta:
          unique_together = ("superid", "name")  
          


     def __str__(self):
        #return str(self.superid)+": "+self.name
        return "%s: %s"%(self.superid, self.name) 

class Currency(models.Model):
      code = models.IntegerField(default=0)
      name = models.CharField(max_length=255)
      description = models.CharField(max_length=255)

     
#      class Meta:
 #        ordering = ('name',)

      def __str__(self):
           return " %s:%s"%(self.name, self.description)


class Country(models.Model):

     country = models.IntegerField(default=0)
     name = models.CharField(max_length=255)
     
   
     class Meta:
       ordering = ('name',)
     
     def __str__(self):
        
        return " %s"%(self.name)


class Ledger(models.Model):

     ledger = models.CharField(max_length=255)
     name = models.CharField(max_length=255)



     def __str__(self):
       
        return "%s: %s"%(self.ledger, self.name)
   


 
class SuperidToLoanLiability(models.Model):
     
     superid = models.ForeignKey(Superid)
     loan = models.ForeignKey(Loan)
     liability = models.ForeignKey(Liability)
     guarantee = models.IntegerField(default=0)
     maturity_date = models.DateField(null=True)
#     ledger =  models.ForeignKey(Ledger)
#     ledger = models.CharField(max_length=255,blank=True)
     ledger = models.ForeignKey(Ledger,blank=True, null=True)
     country_of_utilization= models.ForeignKey(Country,blank=True, null=True)
#     country_of_utilization= models.CharField(max_length=255)
     currency = models.ForeignKey(Currency,blank=True, null=True)
     #currency = models.CharField(max_length=255)
     closed = models.BooleanField(default=False)     
 
     if closed == True:
      self.fields['guarantee'].required = False
      self.fields['maturity_date'].required= False
    #  self.fields['ledger'].required= False
     # self.fields['country_of_utilization'].required= False
      guarantee = forms.IntegerField(required=False, blank=True, null=True)    
     # ledger = forms.CharField(required=False, blank=True, null=True)
      country_of_utilization = forms.CharField(required=False, blank=True, null=True)
      

     def __str__(self):
       # return "%s: %s,%s,%s, %s,%s,%s, %s, %s"%(self.superid, self.loan, self.liability, self.guarantee, self.maturity_date, self.country_of_utilization,self.ledger,self.closed)
         return "%s: %s,%s,%s, %s,%s"%(self.superid, self.loan, self.liability, self.guarantee, self.maturity_date,self.closed)



