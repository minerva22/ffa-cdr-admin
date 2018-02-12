from django.contrib import admin
from .models import Superid, Loan, Liability, SuperidToLoanLiability, Country,Currency, Ledger, Entity, Partner_type



admin.site.register(Superid,admin.ModelAdmin)

admin.site.register(Liability,admin.ModelAdmin)
admin.site.register(Loan,admin.ModelAdmin)
admin.site.register(Country,admin.ModelAdmin)
admin.site.register(Currency,admin.ModelAdmin)
admin.site.register(Ledger,admin.ModelAdmin)
admin.site.register(Entity,admin.ModelAdmin)
admin.site.register(Partner_type,admin.ModelAdmin)



admin.site.register(SuperidToLoanLiability,admin.ModelAdmin)
