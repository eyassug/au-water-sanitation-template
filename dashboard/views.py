from django.shortcuts import render, render_to_response
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.forms import CountryStatusForm, FacilityAccessForm, SectorPerformanceForm
from dashboard.forms import DFacilityAccessForm, PriorityAreaStatusForm, DTechnologyForm,DTenderProcPerformanceForm
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PlanningPerformance, TenderProcedurePerformance, CommunityApproach, PartnerContribution, PartnerEventContribution, SWOT, PriorityAreaStatus
from dashboard.models import Country, PriorityArea, SectorCategory, FacilityCharacter, Technology, TenderProcedureProperty
from dashboard import models
from dashboard.models import PriorityAreaStatus
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import LoginForm
from dashboard.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import password_change
from django.forms.models import modelform_factory
from django import forms
from django.contrib import messages
# html to pdf imports
from cgi import escape
#from xhtml2pdf import pisa # TODO: Change this when the lib changes.
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
import StringIO
import os
from django.forms.util import ErrorList
from dashboard import reports
import xhtml2pdf.pisa as pisa 
from dashboard import report_forms
# html to pdf example

    



# Sector Performance Category
class SectorPerformanceCreate(LoginRequiredMixin,CreateView):
    model = SectorPerformance
    template_name = 'sector_performance_form.html'
    def get(self, request,id=None):
        user_country = request.user.usercountry.country        
        if(id):
            instance = models.SectorPerformance.objects.get(pk=int(id))
            form = SectorPerformanceForm(instance=instance)
        else:
            form = SectorPerformanceForm(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})
        data = models.SectorPerformance.objects.filter(country=user_country)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data':data
        })
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(SectorPerformance, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        data = models.SectorPerformance.objects.filter(country=user_country)
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/SectorPerformance')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    
    
class FacilityAccessCreate(LoginRequiredMixin,View):
    def get(self,request, id=None):
        user_country = request.user.usercountry.country
        if(id):
            instance=models.FacilityAccess.objects.get(pk=int(id))
            form=DFacilityAccessForm(instance=instance,initial={
                    'sector_category':instance.technology.facility_character.sector_category,
                    'priority_area':instance.priority_area,
                    'facility_character':instance.technology.facility_character,
                    'technology':instance.technology
                })
        else:
            form = DFacilityAccessForm()
        
        form.filter(country=user_country)
        data = models.FacilityAccess.objects.all()
        return render(request, 'facility_access_form.html', {
            'form': form,
            'country': user_country,
            'data':data
        })
    
    def post(self,request, id=None):
        form = DFacilityAccessForm(request.POST)
        user_country = request.user.usercountry.country
        data = models.FacilityAccess.objects.all()
        if form.is_valid():
            if(id):
                form.instance.id = int(id)
            tech_id = form.cleaned_data['technology']
            try:
                technology = Technology.objects.get(pk=tech_id)
            except Technology.DoesNotExist:
                technology = None
            
            if not (technology):
                form._errors["technology"] = ErrorList([u"This field is required"])
                return render(request, 'facility_access_form.html', {
                    'form': form,
                    'country': user_country,
                    'data':data
                })
    
            form.instance.technology = technology
            form.save()
            if (request.POST.has_key('save_add')):
                new_form = DFacilityAccessForm(initial={'priority_area':form.instance.priority_area,
                                                        'sector_category':form.cleaned_data['sector_category'],
                                                        'facility_character':form.instance.technology.facility_character,
                                                        'technology':form.instance.technology
                                                        })                
                return render(request, 'facility_access_form.html', {
                    'form': new_form,
                    'country': user_country,
                    'data':data,
                    'facility_character':form.cleaned_data['facility_character'],
                    'technology':form.cleaned_data['technology']
                })
            return HttpResponseRedirect('/report/facilityaccess#list')
        return render(request, 'facility_access_form.html', {
            'form': form,
            'country': user_country,
            'data':data
        })
    
class CountryStatusCreate(LoginRequiredMixin,View):
    model = CountryDemographic
    template_name = 'country_status_form.html'
    success_url = "/report/countrystatus"
    
    def get(self,request,id=None):
        user_country = request.user.usercountry.country
        if(id):
            instance = models.CountryDemographic.objects.get(pk=int(id))
            form = CountryStatusForm(instance=instance)
        else:
            form = CountryStatusForm()
        form.instance.country = user_country
        data = models.CountryDemographic.objects.filter(country=user_country)
        return render(request, self.template_name, {
            'form': form,
            'country': user_country,
            'data':data
        })
    
    def post(self,request,id=None):
        user_country = request.user.usercountry.country
        form = CountryStatusForm(request.POST)
        if(form.is_valid()):
            form.instance.country = user_country
            if(id):
                form.instance.id = int(id)
            ins = form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if(request.POST.has_key('save_add')):
                new_form = CountryStatusForm(initial={'country':user_country,'year':form.instance.year})
                new_form.instance.country = user_country
                new_form.instance.year = form.instance.year
                new_form.instance.population = 0
                data = models.CountryDemographic.objects.filter(country=user_country)
                return render(request, self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data':data
                })
            return HttpResponseRedirect(self.success_url+'#list')
        return render(request, self.template_name, {
            'form': form,
            'country': user_country
        })
class PriorityAreaStatusCreate(LoginRequiredMixin,View):
    
    def get(self, request,id=None):        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PriorityAreaStatus.objects.get(pk=int(id))
            form = PriorityAreaStatusForm(instance=instance)
        else:
            form = PriorityAreaStatusForm()
            form.filter(country=user_country)
        #data = models.PriorityAreaStatus.objects.all()
        data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)

        return render(request,'priority_area_status_form.html', {
            'form': form,
            'country': user_country,
            'data':data
        })    
    
    def post(self,request,id=None):
        user_country = request.user.usercountry.country            
        form = PriorityAreaStatusForm(request.POST)
        data = models.PriorityAreaStatus.objects.all()
        if form.is_valid():            
            if(id):
                form.instance.id = int(id)
            form.save()            
            new_form = PriorityAreaStatusForm()
            messages.success(request, 'Report has been successfully submitted.')
            new_form.filter(country=user_country)
            if (request.POST.has_key('save_add')):
                new_form = PriorityAreaStatusForm(initial={'priority_area':form.cleaned_data['priority_area']})                
                return render(request,'priority_area_status_form.html', {
                    'form': new_form,
                    'country': user_country,
                    'data':data
                })
            return HttpResponseRedirect('/report/prioritystatus#list')
        return render(request, 'priority_area_status_form.html', {'form': form})
    
class PlanningPerformanceCreate(LoginRequiredMixin,View):
    model = PlanningPerformance
    template_name = 'planning_performance_form.html'
    success_url = "/report/PlanningPerformance"
    
    def get(self, request,id=None):
        form_class = modelform_factory(PlanningPerformance)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PlanningPerformance.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})
        data = models.PlanningPerformance.objects.filter(country=user_country)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PlanningPerformance, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        data = models.PlanningPerformance.objects.filter(country=user_country)
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/planningperformance')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    
class TenderProcedurePerformanceCreate(LoginRequiredMixin,View):
    model = TenderProcedurePerformance
    template_name = 'tender_proc_performance_form.html'
    success_url = "/report/TenderProcPerformance"
    def get(self, request,id=None):
        if(id):
            instance = TenderProcedurePerformance.objects.get(pk=int(id))
            form = DTenderProcPerformanceForm(instance=instance,initial={'sector_category':instance.tender_procedure_property.sector_category,'tender_procedure_property':instance.tender_procedure_property})
            #form.filter(instance.tender_procedure_property.sector_category)
        else:
            form = DTenderProcPerformanceForm(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})      
        user_country = request.user.usercountry.country
        data = models.TenderProcedurePerformance.objects.filter(country=user_country)

        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form = DTenderProcPerformanceForm(request.POST)
        form.instance.country = user_country
        data = models.TenderProcedurePerformance.objects.filter(country=user_country)
        if(form.is_valid()):
            form.instance.country = user_country
            if(id):
                form.instance.id=int(id)
            prop_id = form.cleaned_data['tender_procedure_property']
            try:
                prop = models.TenderProcedureProperty.objects.get(pk=prop_id)
            except models.TenderProcedureProperty.DoesNotExist:
                prop = None
            form.instance.tender_procedure_property = prop
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'tender_procedure_property':form.cleaned_data['tender_procedure_property']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/TenderProcPerformance')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })

class CommunityApproachCreate(LoginRequiredMixin,View):
    model = CommunityApproach
    template_name = 'community_approach_form.html'
    success_url = "/report/CommunityApproach"
    def get(self, request, id=None):
        form_class = modelform_factory(CommunityApproach)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.CommunityApproach.objects.get(pk=int(id))
            form=form_class(instance=instance)
        else:
            form=form_class(initial={'approach_name':"", 'description':"",'lessons_learnt':''})
        data = models.CommunityApproach.objects.all()
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(CommunityApproach, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        data = models.CommunityApproach.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'approach_type':form.cleaned_data['approach_type'], 'sector_category':form.cleaned_data['sector_category']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/communityapproach')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    
class PartnerContributionCreate(LoginRequiredMixin,CreateView):
    model = PartnerContribution
    template_name = 'partner_contribution_form.html'
    success_url = "/report/PartnerContribution"
    def get(self, request, id=None):
        form_class = modelform_factory(PartnerContribution)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PartnerContribution.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class(initial={'in_kind_contribution':'','financial_contribution':'', 'annual_contribution':''})
        data = models.PartnerContribution.objects.all()
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PartnerContribution, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        data = models.PartnerContribution.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'partner':form.cleaned_data['partner']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/PartnerContribution')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
class PartnerEventContributionCreate(LoginRequiredMixin,CreateView):
    model = PartnerEventContribution
    template_name = 'partner_event_contribution_form.html'
    success_url = "/report/PartnerEventContribution"
    def get(self, request, id=None):
        form_class = modelform_factory(PartnerEventContribution)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PartnerEventContribution.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class()
        data = models.PartnerEventContribution.objects.all()
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data    
        })
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PartnerEventContribution, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        data = models.PartnerEventContribution.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'partner':form.cleaned_data['partner'], 'event':form.cleaned_data['event']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/PartnerEventContribution')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
class SWOTAndConclusionCreate(LoginRequiredMixin,View):
    model = SWOT
    template_name = 'swot_form.html'
    success_url = "/report/swot"
    def get(self, request, id=None):
        form_class = modelform_factory(SWOT)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.SWOT.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class(initial={'strengths':'', 'opportunities':'','mitigation_measures':'','overall_challenges':'','kap_recommendations':'','risks':'','weaknesses':'','conclusion':''})
        data = models.SWOT.objects.all()
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    def post(self, request):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(SWOT,exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        data = models.SWOT.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})                
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/swot')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
    
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

def feed_tender_proc_properties(request, sector_category_id):
    sector_category = SectorCategory.objects.get(pk=sector_category_id)
    properties = TenderProcedureProperty.objects.filter(sector_category=sector_category)
    return render_to_response('feeds/tender_proc_properties.txt', {'properties':properties}, mimetype="text/plain")

class TechnologyCreate(LoginRequiredMixin,View):
    def get(self,request):
        form = DTechnologyForm()
        return render(request, 'technology_admin.html', {'form': form})
    
    def post(self, request):
        form = DTechnologyForm(request.POST)
        if(form.is_valid()):
            fc_id = form.cleaned_data['facility_character']
            facility_character = FacilityCharacter.objects.get(pk=fc_id)
            form.instance.facility_character = facility_character
            form.save()
            messages.success(request, 'Report has been successfully submitted.')
            if(request.POST['_addanother']):
                return HttpResponseRedirect('/admin/dashboard/technology/add/')
            return HttpResponseRedirect('/admin/dashboard/technology/')
            
        return render(request, 'technology_admin.html', {'form': form})

class CountryDemographicGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.CountryDemographic.objects.filter(country=user_country)
        return render(request, 'data-grids/country_demographic_grid.html', {'data': data})

class PAStatusGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.PriorityAreaStatus.objects.all()
        return render(request, 'data-grids/priority_area_status_grid.html', {'data': data})
    
class TechnologyAccessGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.FacilityAccess.objects.all()
        return render(request, 'data-grids/technology_access_grid.html', {'data': data})
    
class SectorPerformanceGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.SectorPerformance.objects.all()
        return render(request, 'data-grids/sector_performance_grid.html', {'data': data})
    
class PlanningPerformanceGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.PlanningPerformance.objects.filter(country=user_country)
        return render(request, 'data-grids/planning_performance_grid.html', {'data': data})

class TPPerformanceGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.TenderProcedurePerformance.objects.filter(country=user_country)
        return render(request, 'data-grids/tender_proc_performance_grid.html', {'data': data})

class CommunityApproachGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.CommunityApproach.objects.filter(country=user_country)
        return render(request, 'data-grids/community_approach_grid.html', {'data': data})
    
class PartnerContributionGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.PartnerContribution.objects.filter(country=user_country)
        return render(request, 'data-grids/partner_contribution_grid.html', {'data': data})
    
class PartnerEventContributionGridView(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        data = models.PartnerEventContribution.objects.filter(country=user_country)
        return render(request, 'data-grids/partner_event_contribution_grid.html', {'data': data})
class ListofPriorityAreasReport(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country
        report_factory = reports.PriorityAreaPopulationReport()
        report = report_factory.generate(user_country)
        return render(request, 'reports/list_of_priority_areas_report.html',report)
    
class TechnologyGapPerPriorityAreaReport(LoginRequiredMixin,View):
    def get(self,request):
        form = report_forms.TechnologyGapByPriorityArea()        
        return render(request, 'reports/technology_gap_per_priority_area_report.html', {'form':form})
    
    def post(self,request):
        form = report_forms.TechnologyGapByPriorityArea(request.POST)
        user_country = request.user.usercountry.country        
        if(form.is_valid()):
            technology = form.cleaned_data['technology']
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            report_factory = reports.TechnologyGapReport()
            report = report_factory.generate(user_country,technology,int(start_year),int(end_year))
            report['form'] = form
            return render(request, 'reports/technology_gap_per_priority_area_report.html', report)            
        return render(request, 'reports/technology_gap_per_priority_area_report.html', {'form':form})
class TechnologiesGapsForTheCategory(LoginRequiredMixin,View):
    def get(self,request):
        form = report_forms.TechnologyGapByCategory()
        return render(request, 'reports/technologies_gaps_for_the_category.html',{'form':form})
    
    def post(self,request):
        form = report_forms.TechnologyGapByCategory(request.POST)
        user_country = request.user.usercountry.country        
        if(form.is_valid()):
            category = form.cleaned_data['sector_category']
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            report_factory = reports.TechnologyGapByCategoryReport()
            report = report_factory.generate(user_country,category,int(start_year),int(end_year))
            report['form'] = form
            return render(request, 'reports/technologies_gaps_for_the_category.html', report)            
        return render(request, 'reports/technologies_gaps_for_the_category.html', {'form':form})

class EstimatedOverallGapsReport(LoginRequiredMixin,View):
    def get(self,request):
        form = report_forms.EstimatedGap()
        return render(request, 'reports/estimated_overall_gaps.html',{'form':form})
    
    def post(self,request):
        form = report_forms.EstimatedGap(request.POST)
        user_country = request.user.usercountry.country        
        if(form.is_valid()):            
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            report_factory = reports.EstimatedGapReport()
            report = report_factory.generate(user_country,int(start_year),int(end_year))
            report['form'] = form
            return render(request, 'reports/estimated_overall_gaps.html', report)            
        return render(request, 'reports/estimated_overall_gaps.html', {'form':form})

   
