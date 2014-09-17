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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import simplejson as json

# html to pdf example

    

class PriorityAreaView(LoginRequiredMixin,CreateView):
    model = PriorityArea
    template_name = 'snippets/priority_area_list.html'
    def get(self, request,id=None):
        user_country = request.user.usercountry.country        
        
        if not request.user.is_superuser:
            data = models.PriorityArea.objects.filter(country=user_country)
        else:
            data = models.PriorityArea.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            
            'country': user_country,
            'data':data,
            'page':page
        })

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
        if not request.user.is_superuser:
            data = models.SectorPerformance.objects.filter(country=user_country)
        else:
            data = models.SectorPerformance.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(SectorPerformance, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.SectorPerformance.objects.filter(country=user_country)
        else:
            data = models.SectorPerformance.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
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
class SectorPerformanceEdit(LoginRequiredMixin,CreateView):
    model = SectorPerformance
    template_name = 'sector_performance_edit_form.html'
    def get(self, request,id=None):
        user_country = request.user.usercountry.country        
        if(id):
            instance = models.SectorPerformance.objects.get(pk=int(id))
            form = SectorPerformanceForm(instance=instance)
        else:
            form = SectorPerformanceForm(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})
        if not request.user.is_superuser:
            data = models.SectorPerformance.objects.filter(country=user_country)
        else:
            data = models.SectorPerformance.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(SectorPerformance, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.SectorPerformance.objects.filter(country=user_country)
        else:
            data = models.SectorPerformance.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
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
    #def sectorperformance(self,request):
        #return render(request, "sector_performance_list.html", {"sectorperformance" : models.SectorPerformance.objects.all()})

class SectorPerformanceDelete(DeleteView):
    model = SectorPerformance
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(SectorPerformanceDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class SectorPerformanceDelete(LoginRequiredMixin,CreateView):
#    model = SectorPerformance
#    template_name = 'sector_performance_form.html'
#    def get(self, request,id=None, delete=None):
#        user_country = request.user.usercountry.country        
#        if(id):
#            instance = models.SectorPerformance.objects.get(pk=int(id))
#            form = SectorPerformanceForm(instance=instance)
#        else:
#            form = SectorPerformanceForm(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})
#        if not request.user.is_superuser:
#            data = models.SectorPerformance.objects.filter(country=user_country)
#        else:
#            data = models.SectorPerformance.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            #if(int(deleteit)==id):     
#            models.SectorPerformance.objects.filter(id=delete).delete()
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data':data,
#            'page':page
#        })
#    def post(self, request,id=None):
#        user_country = request.user.usercountry.country            
#        form_class = modelform_factory(SectorPerformance, exclude=['country'])
#        form = form_class(request.POST)
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.SectorPerformance.objects.filter(country=user_country)
#        else:
#            data = models.SectorPerformance.objects.all()
#        if(form.is_valid()):
#            if(id):
#                form.instance.id = int(id)
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
#            if (request.POST.has_key('save_add')):
#                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})                
#                return render(request,self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data': data
#                })
#            return HttpResponseRedirect('/report/SectorPerformance')
#        
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data
#        })    
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
        if not request.user.is_superuser:
            data = models.FacilityAccess.objects.filter(priority_area__country=user_country)
        else:
            data = models.FacilityAccess.objects.all()
        paginator = Paginator(data, 2000)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        
        return render(request, 'facility_access_form.html', {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })
    
    def post(self,request, id=None):
        form = DFacilityAccessForm(request.POST)
        user_country = request.user.usercountry.country
        if not request.user.is_superuser:
            data = models.FacilityAccess.objects.filter(priority_area__country=user_country)
        else:
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
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Priority Area '+ str(form.instance.priority_area) + ' and Year '+ str(form.instance.year) + ' and Technology '+ str(form.instance.technology))
            if (request.POST.has_key('save_add')):
                new_form = DFacilityAccessForm(initial={'priority_area':form.instance.priority_area,
                                                        'sector_category':form.cleaned_data['sector_category'],
                                                        'facility_character':form.instance.technology.facility_character,
                                                        'technology':form.instance.technology
                                                        })
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request, 'facility_access_form.html', {
                    'form': new_form,
                    'country': user_country,
                    'data':data,
                    'facility_character':form.cleaned_data['facility_character'],
                    'technology':form.cleaned_data['technology'],
                    'page':page
                    
                })
            return HttpResponseRedirect('/report/facilityaccess#list')
        return render(request, 'facility_access_form.html', {
            'form': form,
            'country': user_country,
            'data':data
        })
class FacilityAccessEdit(LoginRequiredMixin,View):
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
        if not request.user.is_superuser:
            data = models.FacilityAccess.objects.filter(priority_area__country=user_country)
        else:
            data = models.FacilityAccess.objects.all()
        paginator = Paginator(data, 2000)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request, 'facility_access_edit_form.html', {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })
    
    def post(self,request, id=None):
        form = DFacilityAccessForm(request.POST)
        user_country = request.user.usercountry.country
        if not request.user.is_superuser:
            data = models.FacilityAccess.objects.filter(priority_area__country=user_country)
        else:
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
                return render(request, 'facility_access_edit_form.html', {
                    'form': form,
                    'country': user_country,
                    'data':data
                })
    
            form.instance.technology = technology
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Priority Area '+ str(form.instance.priority_area) + ' and Year '+ str(form.instance.year) + ' and Technology '+ str(form.instance.technology))
            if (request.POST.has_key('save_add')):
                new_form = DFacilityAccessForm(initial={'priority_area':form.instance.priority_area,
                                                        'sector_category':form.cleaned_data['sector_category'],
                                                        'facility_character':form.instance.technology.facility_character,
                                                        'technology':form.instance.technology
                                                        })                
                return render(request, 'facility_access_edit_form.html', {
                    'form': new_form,
                    'country': user_country,
                    'data':data,
                    'facility_character':form.cleaned_data['facility_character'],
                    'technology':form.cleaned_data['technology']
                })
            return HttpResponseRedirect('/report/facilityaccess#list')
        return render(request, 'facility_access_edit_form.html', {
            'form': form,
            'country': user_country,
            'data':data
        })
class FacilityAccessDelete(DeleteView):
    model = FacilityAccess
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(FacilityAccessDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class FacilityAccessDelete(LoginRequiredMixin,View):
#    def get(self,request, id=None, delete=None):
#        user_country = request.user.usercountry.country
#        if(id):
#            instance=models.FacilityAccess.objects.get(pk=int(id))
#            form=DFacilityAccessForm(instance=instance,initial={
#                    'sector_category':instance.technology.facility_character.sector_category,
#                    'priority_area':instance.priority_area,
#                    'facility_character':instance.technology.facility_character,
#                    'technology':instance.technology
#                })
#        else:
#            form = DFacilityAccessForm()
#        
#        form.filter(country=user_country)
#        if not request.user.is_superuser:
#            data = models.FacilityAccess.objects.filter(priority_area__country=user_country)
#        else:
#            data = models.FacilityAccess.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.FacilityAccess.objects.filter(id=delete).delete()
#        
#        return render(request, 'facility_access_form.html', {
#            'form': form,
#            'country': user_country,
#            'data':data,
#            'page':page
#        })
#    
#    def post(self,request, id=None):
#        form = DFacilityAccessForm(request.POST)
#        user_country = request.user.usercountry.country
#        if not request.user.is_superuser:
#            data = models.FacilityAccess.objects.filter(priority_area__country=user_country)
#        else:
#            data = models.FacilityAccess.objects.all()
#        
#        if form.is_valid():
#            if(id):
#                form.instance.id = int(id)
#            tech_id = form.cleaned_data['technology']
#            try:
#                technology = Technology.objects.get(pk=tech_id)
#            except Technology.DoesNotExist:
#                technology = None
#            
#            if not (technology):
#                form._errors["technology"] = ErrorList([u"This field is required"])
#                return render(request, 'facility_access_form.html', {
#                    'form': form,
#                    'country': user_country,
#                    'data':data
#                })
#    
#            form.instance.technology = technology
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Priority Area '+ str(form.instance.priority_area) + ' and Year '+ str(form.instance.year) + ' and Technology '+ str(form.instance.technology))
#            if (request.POST.has_key('save_add')):
#                new_form = DFacilityAccessForm(initial={'priority_area':form.instance.priority_area,
#                                                        'sector_category':form.cleaned_data['sector_category'],
#                                                        'facility_character':form.instance.technology.facility_character,
#                                                        'technology':form.instance.technology
#                                                        })                
#                return render(request, 'facility_access_form.html', {
#                    'form': new_form,
#                    'country': user_country,
#                    'data':data,
#                    'facility_character':form.cleaned_data['facility_character'],
#                    'technology':form.cleaned_data['technology']
#                })
#            return HttpResponseRedirect('/report/facilityaccess#list')
#        return render(request, 'facility_access_form.html', {
#            'form': form,
#            'country': user_country,
#            'data':data
#        })
class CountryStatusCreate(LoginRequiredMixin,View):
    model = CountryDemographic
    template_name = 'country_status_form.html'
    success_url = "/report/countrystatus"
    #data = models.CountryDemographic.objects.filter(country=user_country)
    
    def get(self,request,id=None, delete=None, deleteit=None):
        user_country = request.user.usercountry.country
        if(id):
            instance = models.CountryDemographic.objects.get(pk=int(id))
            form = CountryStatusForm(instance=instance)
        else:
            form = CountryStatusForm()
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.CountryDemographic.objects.filter(country=user_country)
        else:
            data = models.CountryDemographic.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        #if((int(delete)!=0)):
        #    if(int(deleteit) == 0):        
        #        #template_name = 'object_confirm_delete.html'
        #        data = models.CountryDemographic.objects.filter(id=19)
        #        return render(request, 'object_confirm_delete.html', {
        #            'form': form,
        #            'country': user_country,
        #            'data':data,
        #            'page':page
        #        })
        #if(int(delete) > 0):
        #    #if(int(deleteit)==id):     
        #    models.CountryDemographic.objects.filter(id=delete).delete()
                #def get_success_url(self):
                    #return reverse('people_list')
                
        return render(request, self.template_name, {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })
    
    
    def post(self,request,id=None, delete=None):
        user_country = request.user.usercountry.country
        form = CountryStatusForm(request.POST)
        if(form.is_valid()):
            form.instance.country = user_country
            if(id):
                form.instance.id = int(id)
            try:
                ins = form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(user_country) + ' and Year '+ str(form.instance.year))
                
            if(request.POST.has_key('save_add')):
                new_form = CountryStatusForm(initial={'country':user_country,'year':form.instance.year})
                new_form.instance.country = user_country
                new_form.instance.year = form.instance.year
                new_form.instance.population = 0
                
                if not request.user.is_superuser:
                    data = models.CountryDemographic.objects.filter(country=user_country)
                else:
                    data = models.CountryDemographic.objects.all()
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request, self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data':data,
                    'page':page
                })
            
            return HttpResponseRedirect(self.success_url+'#list')
        return render(request, self.template_name, {
            'form': form,
            'country': user_country,
            'data':data
        })

class CountryStatusEdit(LoginRequiredMixin,View):
    model = CountryDemographic
    template_name = 'country_status_edit_form.html'
    success_url = "/report/countrystatus"
    
    def get(self,request,id=None):
        user_country = request.user.usercountry.country
        if(id):
            instance = models.CountryDemographic.objects.get(pk=int(id))
            form = CountryStatusForm(instance=instance)
        else:
            form = CountryStatusForm()
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.CountryDemographic.objects.filter(country=user_country)
        else:
            data = models.CountryDemographic.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request, self.template_name, {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })
    
    def post(self,request,id=None):
        user_country = request.user.usercountry.country
        form = CountryStatusForm(request.POST)
        if(form.is_valid()):
            form.instance.country = user_country
            if(id):
                form.instance.id = int(id)
            try:
                ins = form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(user_country) + ' and Year '+ str(form.instance.year))
            if(request.POST.has_key('save_add')):
                new_form = CountryStatusForm(initial={'country':user_country,'year':form.instance.year})
                new_form.instance.country = user_country
                new_form.instance.year = form.instance.year
                new_form.instance.population = 0
                if not request.user.is_superuser:
                    data = models.CountryDemographic.objects.filter(country=user_country)
                else:
                    data = models.CountryDemographic.objects.all()
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
    
class CountryStatusDelete(DeleteView):
    model = CountryDemographic
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(CountryStatusDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class CountryStatusDelete(LoginRequiredMixin,View):
#    model = CountryDemographic
#    template_name = 'country_status_form.html'
#    success_url = "/report/countrystatus"
#    #data = models.CountryDemographic.objects.filter(country=user_country)
#    
#    def get(self,request,id=None, delete=None, deleteit=None):
#        user_country = request.user.usercountry.country
#        if(id):
#            instance = models.CountryDemographic.objects.get(pk=int(id))
#            form = CountryStatusForm(instance=instance)
#        else:
#            form = CountryStatusForm()
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.CountryDemographic.objects.filter(country=user_country)
#        else:
#            data = models.CountryDemographic.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        #if((int(delete)!=0)):
#        #    if(int(deleteit) == 0):        
#        #        #template_name = 'object_confirm_delete.html'
#        #        data = models.CountryDemographic.objects.filter(id=19)
#        #        return render(request, 'object_confirm_delete.html', {
#        #            'form': form,
#        #            'country': user_country,
#        #            'data':data,
#        #            'page':page
#        #        })
#        if(int(delete) > 0):
#            #if(int(deleteit)==id):     
#            models.CountryDemographic.objects.filter(id=delete).delete()
#                #def get_success_url(self):
#                    #return reverse('people_list')
#                
#        return render(request, self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data':data,
#            'page':page
#        })
#    def post(self,request,id=None, delete=None):
#        user_country = request.user.usercountry.country
#        form = CountryStatusForm(request.POST)
#        if(form.is_valid()):
#            form.instance.country = user_country
#            if(id):
#                form.instance.id = int(id)
#            try:
#                ins = form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(user_country) + ' and Year '+ str(form.instance.year))
#                
#            if(request.POST.has_key('save_add')):
#                new_form = CountryStatusForm(initial={'country':user_country,'year':form.instance.year})
#                new_form.instance.country = user_country
#                new_form.instance.year = form.instance.year
#                new_form.instance.population = 0
#                if not request.user.is_superuser:
#                    data = models.CountryDemographic.objects.filter(country=user_country)
#                else:
#                    data = models.CountryDemographic.objects.all()
#                return render(request, self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data':data
#                })
#            
#            return HttpResponseRedirect(self.success_url+'#list')
#        return render(request, self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data':data
#        })
class PriorityAreaStatusCreate(LoginRequiredMixin,View):
    
    def get(self, request,id=None):        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PriorityAreaStatus.objects.get(pk=int(id))
            form = PriorityAreaStatusForm(instance=instance)
        else:
            form = PriorityAreaStatusForm()
            
        form.filter(country=user_country)
        if not request.user.is_superuser:
            data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)
        else:
            data = models.PriorityAreaStatus.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
                            
        return render(request,'priority_area_status_form.html', {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })    
    
    def post(self,request,id=None):
        user_country = request.user.usercountry.country            
        form = PriorityAreaStatusForm(request.POST)
        form.filter(country=user_country)
        if not request.user.is_superuser:
            data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)
        else:
            data = models.PriorityAreaStatus.objects.all()

        if form.is_valid():
            
            if(id):
                form.instance.id = int(id)
            try:
                ins = form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Priority Area: '+ str(form.instance.priority_area) + ' and Year '+ str(form.instance.year))
                messages.show()
            except:
                messages.error(request,'An unexpected error occured.\n'+ str(sys.exc_info()[0]) + '\n'+ str(ex))
                messages.show()
                
            if (request.POST.has_key('save_add')):
                new_form = PriorityAreaStatusForm(initial={'priority_area':form.cleaned_data['priority_area']})
                new_form.filter(country=user_country)
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,'priority_area_status_form.html', {
                    'form': new_form,
                    'country': user_country,
                    'data':data,
                    'page':page
                })
            return HttpResponseRedirect('/report/prioritystatus')
        return render(request, 'priority_area_status_form.html', {'form': form,'country':user_country,'data':data})
 
class PriorityAreaStatusEdit(LoginRequiredMixin,View):
    
    def get(self, request,id=None):        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PriorityAreaStatus.objects.get(pk=int(id))
            form = PriorityAreaStatusForm(instance=instance)
        else:
            form = PriorityAreaStatusForm()
            
        form.filter(country=user_country)
        if not request.user.is_superuser:
            data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)
        else:
            data = models.PriorityAreaStatus.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
                            
        return render(request,'priority_area_status_edit_form.html', {
            'form': form,
            'country': user_country,
            'data':data,
            'page':page
        })    
    
    def post(self,request,id=None):
        user_country = request.user.usercountry.country            
        form = PriorityAreaStatusForm(request.POST)
        form.filter(country=user_country)
        if not request.user.is_superuser:
            data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)
        else:
            data = models.PriorityAreaStatus.objects.all()

        if form.is_valid():
            
            if(id):
                form.instance.id = int(id)
            try:
                ins = form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Priority Area: '+ str(form.instance.priority_area) + ' and Year '+ str(form.instance.year))
                messages.show()
            except:
                messages.error(request,'An unexpected error occured.\n'+ str(sys.exc_info()[0]) + '\n'+ str(ex))
                messages.show()
                
            if (request.POST.has_key('save_add')):
                new_form = PriorityAreaStatusForm(initial={'priority_area':form.cleaned_data['priority_area']})
                new_form.filter(country=user_country)
                return render(request,'priority_area_status_form.html', {
                    'form': new_form,
                    'country': user_country,
                    'data':data
                })
            return HttpResponseRedirect('/report/prioritystatus')
        return render(request, 'priority_area_status_edit_form.html', {'form': form,'country':user_country,'data':data})

class PriorityAreaStatusDelete(DeleteView):
    model = PriorityAreaStatus
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(PriorityAreaStatusDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class PriorityAreaStatusDelete(LoginRequiredMixin,View):
#    
#    def get(self, request,id=None, delete=None):        
#        user_country = request.user.usercountry.country
#        if(id):
#            instance = models.PriorityAreaStatus.objects.get(pk=int(id))
#            form = PriorityAreaStatusForm(instance=instance)
#        else:
#            form = PriorityAreaStatusForm()
#            
#        form.filter(country=user_country)
#        if not request.user.is_superuser:
#            data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)
#        else:
#            data = models.PriorityAreaStatus.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.PriorityAreaStatus.objects.filter(id=delete).delete()
#                            
#        return render(request,'priority_area_status_form.html', {
#            'form': form,
#            'country': user_country,
#            'data':data,
#            'page':page
#        })    
#    
#    def post(self,request,id=None, delete=None):
#        user_country = request.user.usercountry.country            
#        form = PriorityAreaStatusForm(request.POST)
#        form.filter(country=user_country)
#        if not request.user.is_superuser:
#            data = models.PriorityAreaStatus.objects.filter(priority_area__country = user_country)
#        else:
#            data = models.PriorityAreaStatus.objects.all()
#
#        if form.is_valid():
#            
#            if(id):
#                form.instance.id = int(id)
#            try:
#                ins = form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Priority Area: '+ str(form.instance.priority_area) + ' and Year '+ str(form.instance.year))
#                messages.show()
#            except:
#                messages.error(request,'An unexpected error occured.\n'+ str(sys.exc_info()[0]) + '\n'+ str(ex))
#                messages.show()
#                
#            if (request.POST.has_key('save_add')):
#                new_form = PriorityAreaStatusForm(initial={'priority_area':form.cleaned_data['priority_area']})
#                new_form.filter(country=user_country)
#                return render(request,'priority_area_status_form.html', {
#                    'form': new_form,
#                    'country': user_country,
#                    'data':data
#                })
#            return HttpResponseRedirect('/report/prioritystatus')
#        return render(request, 'priority_area_status_form.html', {'form': form,'country':user_country,'data':data})
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
        if not request.user.is_superuser:
            data = models.PlanningPerformance.objects.filter(country=user_country)
        else:
            data = models.PlanningPerformance.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PlanningPerformance, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.PlanningPerformance.objects.filter(country=user_country)
        else:
            data = models.PlanningPerformance.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data,
                    'page':page
                })
            return HttpResponseRedirect('/report/planningperformance')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })

class PlanningPerformanceEdit(LoginRequiredMixin,View):
    model = PlanningPerformance
    template_name = 'planning_performance_edit_form.html'
    success_url = "/report/PlanningPerformance"
    
    def get(self, request,id=None):
        form_class = modelform_factory(PlanningPerformance)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PlanningPerformance.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})
        if not request.user.is_superuser:
            data = models.PlanningPerformance.objects.filter(country=user_country)
        else:
            data = models.PlanningPerformance.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PlanningPerformance, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.PlanningPerformance.objects.filter(country=user_country)
        else:
            data = models.PlanningPerformance.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
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
class PlanningPerformanceDelete(DeleteView):
    model = PlanningPerformance
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(PlanningPerformanceDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class PlanningPerformanceDelete(LoginRequiredMixin,View):
#    model = PlanningPerformance
#    template_name = 'planning_performance_form.html'
#    success_url = "/report/PlanningPerformance"
#    
#    def get(self, request,id=None, delete=None):
#        form_class = modelform_factory(PlanningPerformance)        
#        user_country = request.user.usercountry.country
#        if(id):
#            instance = models.PlanningPerformance.objects.get(pk=int(id))
#            form = form_class(instance=instance)
#        else:
#            form = form_class(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})
#        if not request.user.is_superuser:
#            data = models.PlanningPerformance.objects.filter(country=user_country)
#        else:
#            data = models.PlanningPerformance.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.PlanningPerformance.objects.filter(id=delete).delete()
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data,
#            'page':page
#        })
#    
#    def post(self, request,id=None):
#        user_country = request.user.usercountry.country            
#        form_class = modelform_factory(PlanningPerformance, exclude=['country'])
#        form = form_class(request.POST)
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.PlanningPerformance.objects.filter(country=user_country)
#        else:
#            data = models.PlanningPerformance.objects.all()
#        if(form.is_valid()):
#            if(id):
#                form.instance.id = int(id)
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
#            if (request.POST.has_key('save_add')):
#                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})                
#                return render(request,self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data': data
#                })
#            return HttpResponseRedirect('/report/planningperformance')
#        
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data
#        })
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
        if not request.user.is_superuser:
            data = models.TenderProcedurePerformance.objects.filter(country=user_country)
        else:
            data = models.TenderProcedurePerformance.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)

        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form = DTenderProcPerformanceForm(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.TenderProcedurePerformance.objects.filter(country=user_country)
        else:
            data = models.TenderProcedurePerformance.objects.all()
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
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Tender Procedure Property '+ str(form.instance.tender_procedure_property) + ' and Year '+ str(form.instance.year))
            
            if (request.POST.has_key('save_add')):
                new_form = DTenderProcPerformanceForm(initial={'sector_category':form.cleaned_data['sector_category'], 'tender_procedure_property':form.cleaned_data['tender_procedure_property']})
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data
                })
            return HttpResponseRedirect('/report/TenderProcPerformance')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })

class TenderProcedurePerformanceEdit(LoginRequiredMixin,View):
    model = TenderProcedurePerformance
    template_name = 'tender_proc_performance_edit_form.html'
    success_url = "/report/TenderProcPerformance"
    def get(self, request,id=None):
        if(id):
            instance = TenderProcedurePerformance.objects.get(pk=int(id))
            form = DTenderProcPerformanceForm(instance=instance,initial={'sector_category':instance.tender_procedure_property.sector_category,'tender_procedure_property':instance.tender_procedure_property})
            #form.filter(instance.tender_procedure_property.sector_category)
        else:
            form = DTenderProcPerformanceForm(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})      
        user_country = request.user.usercountry.country
        if not request.user.is_superuser:
            data = models.TenderProcedurePerformance.objects.filter(country=user_country)
        else:
            data = models.TenderProcedurePerformance.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)

        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
            
        })
    def post(self, request,id=None):
        user_country = request.user.usercountry.country            
        form = DTenderProcPerformanceForm(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.TenderProcedurePerformance.objects.filter(country=user_country)
        else:
            data = models.TenderProcedurePerformance.objects.all()
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
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Tender Procedure Property '+ str(form.instance.tender_procedure_property) + ' and Year '+ str(form.instance.year))
            
            if (request.POST.has_key('save_add')):
                new_form = DTenderProcPerformanceForm(initial={'sector_category':form.cleaned_data['sector_category'], 'tender_procedure_property':form.cleaned_data['tender_procedure_property']})
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

class TenderProcedurePerformanceDelete(DeleteView):
    model = TenderProcedurePerformance
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(TenderProcedurePerformanceDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class TenderProcedurePerformanceDelete(LoginRequiredMixin,View):
#    model = TenderProcedurePerformance
#    template_name = 'tender_proc_performance_form.html'
#    success_url = "/report/TenderProcPerformance"
#    def get(self, request,id=None, delete=None):
#        if(id):
#            instance = TenderProcedurePerformance.objects.get(pk=int(id))
#            form = DTenderProcPerformanceForm(instance=instance,initial={'sector_category':instance.tender_procedure_property.sector_category,'tender_procedure_property':instance.tender_procedure_property})
#            #form.filter(instance.tender_procedure_property.sector_category)
#        else:
#            form = DTenderProcPerformanceForm(initial={'success_challenges':'','general_comment':'','bottlenecks':'','measures_taken':''})      
#        user_country = request.user.usercountry.country
#        if not request.user.is_superuser:
#            data = models.TenderProcedurePerformance.objects.filter(country=user_country)
#        else:
#            data = models.TenderProcedurePerformance.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.TenderProcedurePerformance.objects.filter(id=delete).delete()
#
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data,
#            'page':page
#        })
#    def post(self, request,id=None):
#        user_country = request.user.usercountry.country            
#        form = DTenderProcPerformanceForm(request.POST)
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.TenderProcedurePerformance.objects.filter(country=user_country)
#        else:
#            data = models.TenderProcedurePerformance.objects.all()
#        if(form.is_valid()):
#            form.instance.country = user_country
#            if(id):
#                form.instance.id=int(id)
#            prop_id = form.cleaned_data['tender_procedure_property']
#            try:
#                prop = models.TenderProcedureProperty.objects.get(pk=prop_id)
#            except models.TenderProcedureProperty.DoesNotExist:
#                prop = None
#            form.instance.tender_procedure_property = prop
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Tender Procedure Property '+ str(form.instance.tender_procedure_property) + ' and Year '+ str(form.instance.year))
#            
#            if (request.POST.has_key('save_add')):
#                new_form = DTenderProcPerformanceForm(initial={'sector_category':form.cleaned_data['sector_category'], 'tender_procedure_property':form.cleaned_data['tender_procedure_property']})
#                return render(request,self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data': data
#                })
#            return HttpResponseRedirect('/report/TenderProcPerformance')
#        
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data
#        })

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
        if not request.user.is_superuser:
            data = models.CommunityApproach.objects.filter(country=user_country)
        else:
            data = models.CommunityApproach.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(CommunityApproach, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.CommunityApproach.objects.filter(country=user_country)
        else:
            data = models.CommunityApproach.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
            
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'approach_type':form.cleaned_data['approach_type'], 'sector_category':form.cleaned_data['sector_category']})
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data,
                    'page':page
                })
            return HttpResponseRedirect('/report/communityapproach')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })

class CommunityApproachEdit(LoginRequiredMixin,View):
    model = CommunityApproach
    template_name = 'community_approach_edit_form.html'
    success_url = "/report/CommunityApproach"
    def get(self, request, id=None):
        form_class = modelform_factory(CommunityApproach)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.CommunityApproach.objects.get(pk=int(id))
            form=form_class(instance=instance)
        else:
            form=form_class(initial={'approach_name':"", 'description':"",'lessons_learnt':''})
        if not request.user.is_superuser:
            data = models.CommunityApproach.objects.filter(country=user_country)
        else:
            data = models.CommunityApproach.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(CommunityApproach, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.CommunityApproach.objects.filter(country=user_country)
        else:
            data = models.CommunityApproach.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ' and Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
            
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
class CommunityApproachDelete(DeleteView):
    model = CommunityApproach
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(CommunityApproachDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp


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
        if not request.user.is_superuser:
            data = models.PartnerContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerContribution.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PartnerContribution, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.PartnerContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerContribution.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ', Sector Category '+ str(form.instance.sector_category) + ' and Partner '+ str(form.instance.partner))
            
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'partner':form.cleaned_data['partner']})
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data,
                    'page':page
                })
            return HttpResponseRedirect('/report/PartnerContribution')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
class PartnerContributionEdit(LoginRequiredMixin,CreateView):
    model = PartnerContribution
    template_name = 'partner_contribution_edit_form.html'
    success_url = "/report/PartnerContribution"
    def get(self, request, id=None):
        form_class = modelform_factory(PartnerContribution)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PartnerContribution.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class(initial={'in_kind_contribution':'','financial_contribution':'', 'annual_contribution':''})
        if not request.user.is_superuser:
            data = models.PartnerContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerContribution.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PartnerContribution, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.PartnerContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerContribution.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ', Sector Category '+ str(form.instance.sector_category) + ' and Partner '+ str(form.instance.partner))
            
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
class PartnerContributionDelete(DeleteView):
    model = PartnerContribution
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(PartnerContributionDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class PartnerContributionDelete(LoginRequiredMixin,CreateView):
#    model = PartnerContribution
#    template_name = 'partner_contribution_form.html'
#    success_url = "/report/PartnerContribution"
#    def get(self, request, id=None, delete=None):
#        form_class = modelform_factory(PartnerContribution)        
#        user_country = request.user.usercountry.country
#        if(id):
#            instance = models.PartnerContribution.objects.get(pk=int(id))
#            form = form_class(instance=instance)
#        else:
#            form = form_class(initial={'in_kind_contribution':'','financial_contribution':'', 'annual_contribution':''})
#        if not request.user.is_superuser:
#            data = models.PartnerContribution.objects.filter(country=user_country)
#        else:
#            data = models.PartnerContribution.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.PartnerContribution.objects.filter(id=delete).delete()
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data,
#            'page':page
#        })
#    def post(self, request, id=None):
#        user_country = request.user.usercountry.country            
#        form_class = modelform_factory(PartnerContribution, exclude=['country'])
#        form = form_class(request.POST)
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.PartnerContribution.objects.filter(country=user_country)
#        else:
#            data = models.PartnerContribution.objects.all()
#        if(form.is_valid()):
#            if(id):
#                form.instance.id = int(id)
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ', Sector Category '+ str(form.instance.sector_category) + ' and Partner '+ str(form.instance.partner))
#            
#            if (request.POST.has_key('save_add')):
#                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'partner':form.cleaned_data['partner']})                
#                return render(request,self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data': data
#                })
#            return HttpResponseRedirect('/report/PartnerContribution')
#        
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data
#        })
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
        if not request.user.is_superuser:
            data = models.PartnerEventContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerEventContribution.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PartnerEventContribution, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.PartnerEventContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerEventContribution.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ', Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
            
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'partner':form.cleaned_data['partner'], 'event':form.cleaned_data['event']})
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data,
                    'page':page
                })
            return HttpResponseRedirect('/report/PartnerEventContribution')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })
class PartnerEventContributionEdit(LoginRequiredMixin,CreateView):
    model = PartnerEventContribution
    template_name = 'partner_event_contribution_Edit_form.html'
    success_url = "/report/PartnerEventContribution"
    def get(self, request, id=None):
        form_class = modelform_factory(PartnerEventContribution)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.PartnerEventContribution.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class()
        if not request.user.is_superuser:
            data = models.PartnerEventContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerEventContribution.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request, id=None):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(PartnerEventContribution, exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.PartnerEventContribution.objects.filter(country=user_country)
        else:
            data = models.PartnerEventContribution.objects.all()
        if(form.is_valid()):
            if(id):
                form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ', Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
            
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
class PartnerEventContributionDelete(DeleteView):
    model = PartnerEventContribution
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(PartnerEventContributionDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class PartnerEventContributionDelete(LoginRequiredMixin,CreateView):
#    model = PartnerEventContribution
#    template_name = 'partner_event_contribution_form.html'
#    success_url = "/report/PartnerEventContribution"
#    def get(self, request, id=None, delete=None):
#        form_class = modelform_factory(PartnerEventContribution)        
#        user_country = request.user.usercountry.country
#        if(id):
#            instance = models.PartnerEventContribution.objects.get(pk=int(id))
#            form = form_class(instance=instance)
#        else:
#            form = form_class()
#        if not request.user.is_superuser:
#            data = models.PartnerEventContribution.objects.filter(country=user_country)
#        else:
#            data = models.PartnerEventContribution.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.PartnerEventContribution.objects.filter(id=delete).delete()
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data,
#            'page':page
#        })
#    def post(self, request, id=None):
#        user_country = request.user.usercountry.country            
#        form_class = modelform_factory(PartnerEventContribution, exclude=['country'])
#        form = form_class(request.POST)
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.PartnerEventContribution.objects.filter(country=user_country)
#        else:
#            data = models.PartnerEventContribution.objects.all()
#        if(form.is_valid()):
#            if(id):
#                form.instance.id = int(id)
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save! Duplicate Entry for Country '+ str(form.instance.country) + ', Sector Category '+ str(form.instance.sector_category) + ' and Year '+ str(form.instance.year))
#            
#            if (request.POST.has_key('save_add')):
#                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category'], 'partner':form.cleaned_data['partner'], 'event':form.cleaned_data['event']})                
#                return render(request,self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data': data
#                })
#            return HttpResponseRedirect('/report/PartnerEventContribution')
#        
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data
#        })
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
        if not request.user.is_superuser:
            data = models.SWOT.objects.filter(country=user_country)
        else:
            data = models.SWOT.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(SWOT,exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.SWOT.objects.filter(country=user_country)
        else:
            data = models.SWOT.objects.all()
        if(form.is_valid()):
            #if(id):
            #    form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save!' )
            
            if (request.POST.has_key('save_add')):
                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})
                paginator = Paginator(data, 30)
                page_num = request.GET.get('page', 1)
                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                except PageNotAnInteger:
                    page = paginator.page(1)
                return render(request,self.template_name, {
                    'form': new_form,
                    'country': user_country,
                    'data': data,
                    'page':page
                })
            return HttpResponseRedirect('/report/swot')
        
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data
        })

class SWOTAndConclusionEdit(LoginRequiredMixin,View):
    model = SWOT
    template_name = 'swot_edit_form.html'
    success_url = "/report/swot"
    def get(self, request, id=None):
        form_class = modelform_factory(SWOT)        
        user_country = request.user.usercountry.country
        if(id):
            instance = models.SWOT.objects.get(pk=int(id))
            form = form_class(instance=instance)
        else:
            form = form_class(initial={'strengths':'', 'opportunities':'','mitigation_measures':'','overall_challenges':'','kap_recommendations':'','risks':'','weaknesses':'','conclusion':''})
        if not request.user.is_superuser:
            data = models.SWOT.objects.filter(country=user_country)
        else:
            data = models.SWOT.objects.all()
        paginator = Paginator(data, 30)
        page_num = request.GET.get('page', 1)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
                page = paginator.page(1)
        return render(request,self.template_name, {
            'form': form,
            'country': user_country,
            'data': data,
            'page':page
        })
    def post(self, request):
        user_country = request.user.usercountry.country            
        form_class = modelform_factory(SWOT,exclude=['country'])
        form = form_class(request.POST)
        form.instance.country = user_country
        if not request.user.is_superuser:
            data = models.SWOT.objects.filter(country=user_country)
        else:
            data = models.SWOT.objects.all()
        if(form.is_valid()):
            #if(id):
            #    form.instance.id = int(id)
            try:
                form.save()
                messages.success(request, 'Report has been successfully submitted.')
            except IntegrityError as e:
                messages.error(request,'Could not Save!' )
            
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
class SWOTDelete(DeleteView):
    model = SWOT
    template_name = "object_confirm_delete.html"
    success_url = "/"
    
    # allow delete only logged in user by appling decorator
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(SWOTDelete, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
#class SWOTAndConclusionDelete(LoginRequiredMixin,View):
#    model = SWOT
#    template_name = 'swot_form.html'
#    success_url = "/report/swot"
#    def get(self, request, id=None, delete=None):
#        form_class = modelform_factory(SWOT)        
#        user_country = request.user.usercountry.country
#        if(id):
#            instance = models.SWOT.objects.get(pk=int(id))
#            form = form_class(instance=instance)
#        else:
#            form = form_class(initial={'strengths':'', 'opportunities':'','mitigation_measures':'','overall_challenges':'','kap_recommendations':'','risks':'','weaknesses':'','conclusion':''})
#        if not request.user.is_superuser:
#            data = models.SWOT.objects.filter(country=user_country)
#        else:
#            data = models.SWOT.objects.all()
#        paginator = Paginator(data, 30)
#        page_num = request.GET.get('page', 1)
#        try:
#            page = paginator.page(page_num)
#        except EmptyPage:
#            page = paginator.page(paginator.num_pages)
#        except PageNotAnInteger:
#                page = paginator.page(1)
#        if(int(delete) > 0):
#            models.SWOT.objects.filter(id=delete).delete()
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data,
#            'page':page
#        })
#    def post(self, request):
#        user_country = request.user.usercountry.country            
#        form_class = modelform_factory(SWOT,exclude=['country'])
#        form = form_class(request.POST)
#        form.instance.country = user_country
#        if not request.user.is_superuser:
#            data = models.SWOT.objects.filter(country=user_country)
#        else:
#            data = models.SWOT.objects.all()
#        if(form.is_valid()):
#            #if(id):
#            #    form.instance.id = int(id)
#            try:
#                form.save()
#                messages.success(request, 'Report has been successfully submitted.')
#            except IntegrityError as e:
#                messages.error(request,'Could not Save!' )
#            
#            if (request.POST.has_key('save_add')):
#                new_form = form_class(initial={'sector_category':form.cleaned_data['sector_category']})                
#                return render(request,self.template_name, {
#                    'form': new_form,
#                    'country': user_country,
#                    'data': data
#                })
#            return HttpResponseRedirect('/report/swot')
#        
#        return render(request,self.template_name, {
#            'form': form,
#            'country': user_country,
#            'data': data
#        })
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
            technology_id = form.cleaned_data['technology']
            #technology = Technology.objects.get(pk = int(technology_id))
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

   
