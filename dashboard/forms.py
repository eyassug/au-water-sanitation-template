from django import forms
from dashboard.models import CountryDemographic, FacilityAccess

class CountryStatusForm(forms.ModelForm):
    class Meta:
        model = CountryDemographic
        
class FacilityAccessForm(forms.ModelForm):
    class Meta:
        model = FacilityAccess