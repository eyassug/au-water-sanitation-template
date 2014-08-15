from django import forms
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PriorityAreaStatus, Technology
from dashboard.models import Country, PriorityArea, SectorCategory, TenderProcedurePerformance, TenderProcedureProperty

class CountryStatusForm(forms.ModelForm):
    class Meta:
        model = CountryDemographic
        exclude = ['country']
        
class FacilityAccessForm(forms.ModelForm):
    class Meta:
        model = FacilityAccess
        exclude = ['technology']
    
    def filter(self, country):
        if country:
            self.fields['priority_area'].queryset = PriorityArea.objects.filter(country=country)
            
class SectorPerformanceForm(forms.ModelForm):
    class Meta:
        model = SectorPerformance
        exclude = ['country']
        
class PriorityAreaStatusForm(forms.ModelForm):
    class Meta:
        model = PriorityAreaStatus        
        
    def filter(self, country):
        if country:
            self.fields['priority_area'].queryset = PriorityArea.objects.filter(country=country)
        
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
    
# Cascade Filters
class DynamicChoiceField(forms.ChoiceField): 
    def clean(self, value): 
        return value
    
class DFacilityAccessForm(FacilityAccessForm):    
    sector_category = forms.ModelChoiceField(required=False,queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologiesNew();'}),)
    technology = DynamicChoiceField(widget=forms.Select(),)

class DPriorityAreaStatusForm(PriorityAreaStatusForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'onchange':'FilterPriorityAreas();'})) 
    priority_area = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Priority Area'),))

class DTenderProcPerformanceForm(forms.ModelForm):
    class Meta:
        model = TenderProcedurePerformance
        exclude = ['tender_procedure_property','country']
    sector_category = forms.ModelChoiceField(required=True,queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterTenderProcProperties();'}))
    tender_procedure_property = DynamicChoiceField(required=True,widget=forms.Select(),)
    
    #def filter(self,sector_category):
    #    self.fields['tender_procedure_property'].queryset = TenderProcedureProperty.objects.filter(sector_category=sector_category)
    #    
class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        exclude = ['facility_character']
    
class DTechnologyForm(TechnologyForm):
    sector_category = forms.ModelChoiceField(queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologies();', 'disabled':'true'}), choices=(('-1','Select Facility Character'),))
    technology = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Technology'),))
    
