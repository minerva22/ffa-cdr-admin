from django.http import HttpResponse
from django.views import generic
from .models import SuperidToLoanLiability


class IndexView( generic.ListView):
    template_name = 'cdradmin/index.html'
    
    model= SuperidToLoanLiability
    

    def get_queryset(self):
        """Return the  location by order alphabetic."""
        return SuperidToLoanLiability.objects.order_by('superid')
   
def show_superid(request):
   form = SuperidForm()
   if request.method == "POST":
      form = SuperidForm(request.POST)
      if form.is_valid:
         #redirect to the url where you'll process the input
         return HttpResponseRedirect('cdradmin/index.html') # insert reverse or url
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'cdradmin/index.html',{
          'form': form,
          'errors': errors,
   })
