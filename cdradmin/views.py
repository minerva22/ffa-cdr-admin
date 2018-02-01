from django.http import HttpResponse
from django.views import generic
from .models import SuperidToLoanLiability
from django.http import JsonResponse
import json
from django.core import serializers
#from django.core.serializers.json import DjangoJSONEncoder
class IndexView( generic.ListView):
    template_name = 'cdradmin/index.html'
    
    model= SuperidToLoanLiability
    

    def get_queryset(self):
        """Return the  location by order alphabetic."""
        return SuperidToLoanLiability.objects.order_by('superid')
   
    def get(self, *args, **kwargs):
    
        asjson = self.request.GET.get('asjson', "false")
        asjson=asjson.lower()=="true"
          
        if not asjson:
            return super(IndexView, self).get(*args, **kwargs)
        
   
        
             
        #https://stackoverflow.com/questions/41116841/object-is-not-json-serializable-django
        #to get the id of foreignkey
        #data = SuperidToLoanLiability.objects.all().values('superid', 'loan', 'liability')
        #data = SuperidToLoanLiability.objects.all()[0]
        json_obj = [
          {
            "superid": x.superid.superid,
            "loan_type": x.loan.short_description,
            "liability_type": x.liability.short_description,
            "ledger": x.ledger.ledger
          } for x in SuperidToLoanLiability.objects.all()
        ]
        return JsonResponse(json_obj ,safe=False)
