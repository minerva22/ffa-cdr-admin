from django.contrib import admin
from .models import Superid, Loan, Liability




class SuperidAdmin(admin.ModelAdmin):  
  list_display = ['superid']
  
  
class LoanAdmin(admin.ModelAdmin):  
  list_display = ['Loshortdescription']
  
  
class LiabilityAdmin(admin.ModelAdmin):  
  list_display = ['Lishortdescription']
  
    



admin.site.register(Superid,SuperidAdmin)

admin.site.register(Liability,LiabilityAdmin)
admin.site.register(Loan,LoanAdmin)
