from __future__ import unicode_literals

from django.db import models


class Loan(models.Model):


     short_description = models.CharField(max_length=255)
     long_description = models.CharField(max_length=600)


     def __str__(self):
        return self.short_description

class Liability(models.Model):
    
      short_description = models.CharField(max_length=255)
      long_description = models.CharField(max_length=600)

      def __str__(self):
        return self.short_description


class Superid(models.Model):
     
     superid = models.IntegerField(default=0)
     name = models.CharField(max_length=255)

     def __str__(self):
        return str(self.superid)+": "+self.name


class SuperidToLoanLiability(models.Model):
     
     superid = models.ForeignKey(Superid)
     loan = models.ForeignKey(Loan)
     liability = models.ForeignKey(Liability)
     

     def __str__(self):
        return "%s: %s, %s"%(self.superid, self.loan, self.liability)


