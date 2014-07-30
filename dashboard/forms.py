from django import forms
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PriorityAreaStatus, Technology
from dashboard.models import Country, PriorityArea, SectorCategory

class CountryStatusForm(forms.ModelForm):
    class Meta:
        model = CountryDemographic
        
class FacilityAccessForm(forms.ModelForm):
    class Meta:
        model = FacilityAccess
        exclude = ['priority_area','technology']
        
class SectorPerformanceForm(forms.ModelForm):
    class Meta:
        model = SectorPerformance
        
class PriorityAreaStatusForm(forms.ModelForm):
    class Meta:
        model = PriorityAreaStatus
        exclude = ['priority_area']
        
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
    
# Cascade Filters
class DynamicChoiceField(forms.ChoiceField): 
    def clean(self, value): 
        return value
    
class DFacilityAccessForm(FacilityAccessForm):    
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'onchange':'FilterPriorityAreas();'})) 
    priority_area = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Priority Area'),))
    sector_category = forms.ModelChoiceField(queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologies();'}), choices=(('-1','Select Facility Character'),))
    technology = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Technology'),))

class DPriorityAreaStatusForm(PriorityAreaStatusForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'onchange':'FilterPriorityAreas();'})) 
    priority_area = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Priority Area'),))
    
class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
    
class DTechnologyForm(TechnologyForm):
    sector_category = forms.ModelChoiceField(queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologies();', 'disabled':'true'}), choices=(('-1','Select Facility Character'),))
    technology = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Technology'),))
    
