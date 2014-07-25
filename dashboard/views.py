from django.shortcuts import render
from django.http import HttpResponseRedirect
from dashboard.forms import CountryStatusForm
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