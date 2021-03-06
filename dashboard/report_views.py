from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from dashboard.mixins import LoginRequiredMixin
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
from dashboard import report_forms,models

class ListofPriorityAreasReportToPdf(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country
        report_factory = reports.PriorityAreaPopulationReport()
        context_dict = report_factory.generate(user_country)
       
        context_dict.update({'pagesize': 'Portrait'})
    
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(os.path.dirname(BASE_DIR), "auwsssp", "static", "templates")
        template_name = "snippets/list_of_priority_areas_report_pdf.html"
        template = get_template(template_name)
        context = Context(context_dict)
        html = template.render(context)   
        result = StringIO.StringIO()
        
        pisa.CreatePDF(html.encode("UTF-8"), result , encoding='UTF-8',
                       link_callback=path)
        try:
            return HttpResponse(result.getvalue(), mimetype='application/pdf')
            
            #""" Enable if you want to generate pdf in a new file """
            response['Content-Disposition'] = 'attachment; filename=output.pdf'
            return response
        except:
            return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
        
class TechnologyGapClusteredByPAReport(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country
        technology_id = int(request.GET['technology'])
        start_year = int(request.GET['start_year'])
        end_year = int(request.GET['end_year'])
        technology = models.Technology.objects.get(id=technology_id)
        report_factory = reports.TechnologyGapReport()
        #report = report_factory.generate(user_country,technology,start_year,end_year)
        
        context_dict = report_factory.generate(user_country,technology,start_year,end_year)
        #
        context_dict.update({'pagesize': 'Portrait'})
    
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(os.path.dirname(BASE_DIR), "auwsssp", "static", "templates")
        template_name = "snippets/technology_gap_clustered_by_pa_report_pdf.html"
        template = get_template(template_name)
        context = Context(context_dict)
        html = template.render(context)   
        result = StringIO.StringIO()
        
        pisa.CreatePDF(html.encode("UTF-8"), result , encoding='UTF-8',
                       link_callback=path)
        try:
            return HttpResponse(result.getvalue(), mimetype='application/pdf')
            
            #""" Enable if you want to generate pdf in a new file """
            response['Content-Disposition'] = 'attachment; filename=output.pdf'
            return response
        except:
            return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

class TechnologiesGapsForTheCategoryReport(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country        
        category_id = int(request.GET['category'])
        start_year = int(request.GET['start_year'])
        end_year = int(request.GET['end_year'])
        report_factory = reports.TechnologyGapByCategoryReport()
        category = models.SectorCategory.objects.get(id=category_id)
        context_dict = report_factory.generate(user_country,category,start_year,end_year)
        context_dict.update({'pagesize': 'Portrait'})
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(os.path.dirname(BASE_DIR), "auwsssp", "static", "templates")
        template_name = "snippets/technologies_gaps_for_the_category_report_pdf.html"
        template = get_template(template_name)
        context = Context(context_dict)
        html = template.render(context)   
        result = StringIO.StringIO()
        
        pisa.CreatePDF(html.encode("UTF-8"), result , encoding='UTF-8',
                       link_callback=path)
        try:
            return HttpResponse(result.getvalue(), mimetype='application/pdf')
            
            #""" Enable if you want to generate pdf in a new file """
            response['Content-Disposition'] = 'attachment; filename=output.pdf'
            return response
        except:
            return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
        
class EstimatedOverallGaps(LoginRequiredMixin,View):
    def get(self,request):
        user_country = request.user.usercountry.country
        
        start_year = int(request.GET['start_year'])
        end_year = int(request.GET['end_year'])
        report_factory = reports.EstimatedGapReport()
        context_dict = report_factory.generate(user_country,start_year,end_year)
        #
        context_dict.update({'pagesize': 'Portrait'})
    
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(os.path.dirname(BASE_DIR), "auwsssp", "static", "templates")
        template_name = "snippets/estimated_overall_gaps_report_pdf.html"
        template = get_template(template_name)
        context = Context(context_dict)
        html = template.render(context)   
        result = StringIO.StringIO()
        
        pisa.CreatePDF(html.encode("UTF-8"), result , encoding='UTF-8',
                       link_callback=path)
        try:
            return HttpResponse(result.getvalue(), mimetype='application/pdf')
            
            #""" Enable if you want to generate pdf in a new file """
            response['Content-Disposition'] = 'attachment; filename=output.pdf'
            return response
        except:
            return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))