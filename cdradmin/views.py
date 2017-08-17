from django.http import HttpResponse
from django.views import generic
from .models import Superid, Liability, Loan


class IndexView( generic.ListView):
    template_name = 'cdradmin/index.html'
    context_object_name = 'superid_list'
    model= Superid
    

    def get_queryset(self):
        """Return the  location by order alphabetic."""
        return Superid.objects.order_by('superid')
   

