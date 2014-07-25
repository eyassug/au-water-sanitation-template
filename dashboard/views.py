from django.shortcuts import render
from django.http import HttpResponseRedirect
from dashboard.forms import CountryStatusForm

def create_coutry_status(request):
    if(request.method == "POST"):
        cs_form = CountryStatusForm(request.POST)
        if(cs_form.is_valid()):
            pass
    else:
        cs_form = CountryStatusForm()
        
    return render(request, 'countrystatusform.html', {'form': cs_form})