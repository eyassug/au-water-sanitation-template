from django.shortcuts import render
from django.http import HttpResponseRedirect
from dashboard.forms import CountryStatusForm, FacilityAccessForm
from dashboard.models import CountryDemographic

def create_coutry_status(request):
    if(request.method == "POST"):
        cs_form = CountryStatusForm(request.POST)
        if(cs_form.is_valid()):
            country_demographic_data = cs_form.save()
            cs_form = CountryStatusForm()
    else:
        cs_form = CountryStatusForm()
        
    return render(request, 'countrystatusform.html', {'form': cs_form})

def facility_access(request):
    if(request.method == "POST"):
        fa_form = FacilityAccessForm(request.POST)
        if(fa_form.is_valid()):
            country_demographic_data = fa_form.save()
            fa_form = FacilityAccessForm()
    else:
        fa_form = FacilityAccessForm()
        
    return render(request, 'facilityaccessform.html', {'form': fa_form})