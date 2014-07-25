from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.forms import CountryStatusForm, FacilityAccessForm, SectorPerformanceForm
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PlanningPerformance, TenderProcedurePerformance
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Sector Performance Category
class SectorPerformanceCreate(CreateView):
    model = SectorPerformance
    template_name = 'sector_performance_form.html'
    
class FacilityAccessCreate(CreateView):
    model = FacilityAccess
    template_name = 'facility_access_form.html'
    
class CountryStatusCreate(CreateView):
    model = CountryDemographic
    template_name = 'country_status_form.html'
    
class PlanningPerformanceCreate(CreateView):
    model = PlanningPerformance
    template_name = 'planning_performance_form.html'

class TenderProcedurePerformanceCreate(CreateView):
    model = TenderProcedurePerformance
    template_name = 'tender_proc_performance_form.html'
    