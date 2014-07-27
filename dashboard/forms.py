from django import forms
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance

class CountryStatusForm(forms.ModelForm):
    class Meta:
        model = CountryDemographic
        
class FacilityAccessForm(forms.ModelForm):
    class Meta:
        model = FacilityAccess
        
class SectorPerformanceForm(forms.ModelForm):
    class Meta:
        model = SectorPerformance
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
    
    