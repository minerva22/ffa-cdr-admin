from __future__ import unicode_literals

from django.db import models

class Superid (models.Model):
     
     superid = models.IntegerField(default=0)
     name = models.CharField(max_length=255)

class Loan (models.Model):

     Losuperid = models.ForeignKey(Superid)
     Loshortdescription = models.CharField(max_length=255)
     LoDescription = models.CharField(max_length=600)

class Liability(models.Model):
    
    Lisuperid = models.ForeignKey(Superid)
    Lishortdescription = models.CharField(max_length=255)
    Lidescription = models.CharField(max_length=600)





