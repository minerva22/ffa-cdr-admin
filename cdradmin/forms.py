from .models import Superid
from django import forms

class SuperidForm(forms.Form):
    superidf = forms.ModelChoiceField(queryset=Superid.objects.all().order_by('superid'))
