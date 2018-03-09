>>> from cdradmin.models import *
>>> xxx=SuperidToLoanLiability.objects.filter(guarantee_for__isnull=False)
>>> a=xxx[0]
>>> rep_led = Ledger.objects.get(ledger='FFAI')
>>> rep_led
<Ledger: FFAI: FFA PRIVATE BANK S.A.L >
>>> a.ledger=rep_led
>>> a.subledger=a.subledger-7
>>> a.save()
>>> a.id
40
>>> xxx.count()
10
>>> for b in xxx:
...   if b.id==a.id: continue
...   b.ledger=rep_led
...   b.subledger=b.subledger-7
...   b.save()

