from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.forms import CountryStatusForm, FacilityAccessForm, SectorPerformanceForm
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PlanningPerformance, TenderProcedurePerformance, CommunityApproach, PartnerContribution, PartnerEventContribution, SWOT
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import LoginForm
from dashboard.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
# Sector Performance Category
class SectorPerformanceCreate(LoginRequiredMixin,CreateView):
    model = SectorPerformance
    template_name = 'sector_performance_form.html'
    
class FacilityAccessCreate(LoginRequiredMixin,CreateView):
    model = FacilityAccess
    template_name = 'facility_access_form.html'
    
class CountryStatusCreate(LoginRequiredMixin,CreateView):
    model = CountryDemographic
    template_name = 'country_status_form.html'
    
class PlanningPerformanceCreate(LoginRequiredMixin,CreateView):
    model = PlanningPerformance
    template_name = 'planning_performance_form.html'

class TenderProcedurePerformanceCreate(LoginRequiredMixin,CreateView):
    model = TenderProcedurePerformance
    template_name = 'tender_proc_performance_form.html'

class CommunityApproachCreate(LoginRequiredMixin,CreateView):
    model = CommunityApproach
    template_name = 'community_approach_form.html'
    
class PartnerContributionCreate(LoginRequiredMixin,CreateView):
    model = PartnerContribution
    template_name = 'partner_contribution_form.html'
    
class PartnerEventContributionCreate(LoginRequiredMixin,CreateView):
    model = PartnerEventContribution
    template_name = 'partner_event_contribution_form.html'

class SWOTAndConclusionCreate(LoginRequiredMixin,CreateView):
    model = SWOT
    template_name = 'swot_form.html'
    
class Login(View):
    def get(self, request):
        auth_err = ''
        if(request.user.is_authenticated()):            
            return HttpResponseRedirect('/')
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form, 'auth_err': auth_err})
    
    def post(self,request):
        login_form = AuthenticationForm(request.POST)
        if(login_form.is_valid()):            
            username = login_form.username
            password = login_form.password
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)                    
                    return HttpResponseRedirect('/')               
        
        return render(request, 'login.html', {'form': login_form})
    
class Logout(View):
    def get(self,request):
        if(request.user.is_authenticated()):
            logout(request)
        return HttpResponseRedirect('/')
    