from django import forms
from dashboard.models import CountryDemographic

class CountryStatusForm(forms.ModelForm):
    class Meta:
        model = CountryDemographic