from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.forms import CountryStatusForm, FacilityAccessForm, SectorPerformanceForm
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PlanningPerformance, TenderProcedurePerformance, CommunityApproach, PartnerContribution, PartnerEventContribution, SWOT
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import LoginForm
from dashboard.mixins import LoginRequiredMixin
# Sector Performance Category
class SectorPerformanceCreate(LoginRequiredMixin,CreateView):
    model = SectorPerformance
    template_name = 'sector_performance_form.html'
    
class FacilityAccessCreate(CreateView):
    model = FacilityAccess
    template_name = 'facility_access_form.html'
    
class CountryStatusCreate(LoginRequiredMixin,CreateView):
    model = CountryDemographic
    template_name = 'country_status_form.html'
    
class PlanningPerformanceCreate(CreateView):
    model = PlanningPerformance
    template_name = 'planning_performance_form.html'

class TenderProcedurePerformanceCreate(CreateView):
    model = TenderProcedurePerformance
    template_name = 'tender_proc_performance_form.html'

class CommunityApproachCreate(CreateView):
    model = CommunityApproach
    template_name = 'community_approach_form.html'
    
class PartnerContributionCreate(CreateView):
    model = PartnerContribution
    template_name = 'partner_contribution_form.html'
    
class PartnerEventContributionCreate(CreateView):
    model = PartnerEventContribution
    template_name = 'partner_event_contribution_form.html'

class SWOTAndConclusionCreate(CreateView):
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
        login_form = LoginForm(request.POST)
        auth_err = ''
        if(login_form.is_valid()):            
            username = login_form.cleaned_data['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    destination_url = '/'
                    if(request.GET['next']):
                        dest = request.GET['next']
                    return HttpResponseRedirect(destination_url)
                else:                    
                    auth_err = 'The account you specified has been disabled. Please contact your administrator!'
            else:
                auth_err = 'Invalid credentials. Please try again!!!'
        else:
            return render(request, 'login.html', {'form': login_form})
        
        login_form = LoginForm(initial={'username': username})
        return render(request, 'login.html', {'form': login_form, 'auth_err': auth_err})
    
class Logout(View):
    def get(self,request):
        if(request.user.is_authenticated()):
            logout(request)
        return HttpResponseRedirect('/')
    