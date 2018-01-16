from django.contrib import admin
from .models import Superid, Loan, Liability, SuperidToLoanLiability, Country,Currency



admin.site.register(Superid,admin.ModelAdmin)

admin.site.register(Liability,admin.ModelAdmin)
admin.site.register(Loan,admin.ModelAdmin)
admin.site.register(Country,admin.ModelAdmin)
admin.site.register(Currency,admin.ModelAdmin)

admin.site.register(SuperidToLoanLiability,admin.ModelAdmin)
