from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.forms import CountryStatusForm, FacilityAccessForm, SectorPerformanceForm
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PlanningPerformance, TenderProcedurePerformance, CommunityApproach, PartnerContribution, PartnerEventContribution, SWOT
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import LoginForm
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
        if(request.user.is_authenticated()):
            return HttpResponseRedirect('/')
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self,request):
        login_form = LoginForm(request.POST)
        
        if(login_form.is_valid()):            
            username = login_form.cleaned_data['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
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
    