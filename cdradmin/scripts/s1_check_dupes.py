# Check if the superid/ledger/subledger/currency can be made unique

from cdradmin.models import *

xxx=SuperidToLoanLiability.objects.values_list('superid__superid', 'ledger__ledger', 'subledger', 'currency_liability__name')
xxx=["%s/%s/%s/%s"%(x1,x2,x3,x4) for x1,x2,x3,x4 in xxx]
xxx.sort()
len(xxx)
len(set(xxx))
for a in xxx: print(a)
