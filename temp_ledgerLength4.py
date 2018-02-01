from cdradmin.models import *
from django.db.models.functions import Length
Ledger.objects.annotate(length=Length('ledger')).exclude(length=4).count() # delete()
