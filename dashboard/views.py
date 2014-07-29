from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.forms import CountryStatusForm, FacilityAccessForm, SectorPerformanceForm
from dashboard.forms import DFacilityAccessForm
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PlanningPerformance, TenderProcedurePerformance, CommunityApproach, PartnerContribution, PartnerEventContribution, SWOT, PriorityAreaStatus
from dashboard.models import Country, PriorityArea, SectorCategory, FacilityCharacter, Technology
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import LoginForm
from dashboard.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import password_change
# Sector Performance Category
class SectorPerformanceCreate(LoginRequiredMixin,CreateView):
    model = SectorPerformance
    template_name = 'sector_performance_form.html'
    
class FacilityAccessCreate(LoginRequiredMixin,View):
    def get(self,request):
        form = DFacilityAccessForm()
        return render(request, 'facility_access_form.html', {'form': form})
    
    def post(self,request):
        form = DFacilityAccessForm(request.POST)
        if form.is_valid():            
            m = form.save(commit=False)
            pa_id = form.cleaned_data['priority_area']
            m.priority_area = PriorityArea.objects.get(pk=pa_id)
            return HttpResponseRedirect('/report/facilityaccess')
        return render(request, 'facility_access_form.html', {'form': form})
    
class CountryStatusCreate(LoginRequiredMixin,CreateView):
    model = CountryDemographic
    template_name = 'country_status_form.html'
    
class PriorityAreaStatusCreate(LoginRequiredMixin,CreateView):
    model = PriorityAreaStatus
    template_name = 'priority_area_status_form.html'
    
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

class ChangePassword(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        return render(request, 'registration/password_reset_form.html', {'form': form})
    
    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            return password_change(request, post_change_redirect='/')
        form = PasswordChangeForm(request.user)
        return render(request, 'registration/password_reset_form.html', {'form': form})
    
def feed_priority_areas(request,country_id):
    country = Country.objects.get(pk=country_id)
    priority_areas = PriorityArea.objects.filter(country=country)
    return render_to_response('feeds/priority_areas.txt', {'priority_areas':priority_areas}, mimetype="text/plain")

def feed_facility_characters(request, sector_category_id):
    sector_category = SectorCategory.objects.get(pk=sector_category_id)
    facility_characters = FacilityCharacter.objects.filter(sector_category=sector_category)
    return render_to_response('feeds/facility_characters.txt', {'facility_characters':facility_characters}, mimetype="text/plain")

def feed_technologies(request, facility_character_id):
    facility_character = FacilityCharacter.objects.get(pk=facility_character_id)
    technologies = Technology.objects.filter(facility_character=facility_character)
    return render_to_response('feeds/technologies.txt', {'technologies':technologies}, mimetype="text/plain")
