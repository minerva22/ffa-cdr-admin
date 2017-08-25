from django.contrib import admin
from .models import Superid, Loan, Liability, SuperidToLoanLiability






admin.site.register(Superid,admin.ModelAdmin)

admin.site.register(Liability,admin.ModelAdmin)
admin.site.register(Loan,admin.ModelAdmin)

admin.site.register(SuperidToLoanLiability,admin.ModelAdmin)
