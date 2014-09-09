from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from dashboard import views, report_views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    
    # Home:
    
    # Grid / for Urls:
    url(r'^(?i)report/countrystatus$', views.CountryStatusCreate.as_view(), name='country_status_create'),
    url(r'^(?i)report/countrystatusedit/(?P<id>[0-9]+)/$', views.CountryStatusEdit.as_view(), name='country_status_create'),
    url(r'^(?i)report/countrystatusDelete/(?P<delete>[0-9]+)/$', views.CountryStatusDelete.as_view(), name='country_status_delete'),
    url(r'^(?i)report/countrystatus/list$', views.CountryDemographicGridView.as_view(), name='country_status_list'),
    url(r'^(?i)report/prioritystatus$', views.PriorityAreaStatusCreate.as_view(), name='country_status_create'),
    url(r'^(?i)report/prioritystatusedit/(?P<id>[0-9]+)/$', views.PriorityAreaStatusEdit.as_view(), name='country_status_create'),
    url(r'^(?i)report/prioritystatusdelete/(?P<delete>[0-9]+)/$', views.PriorityAreaStatusDelete.as_view(), name='country_status_delete'),
    url(r'^(?i)report/prioritystatus/list$', views.PAStatusGridView.as_view(), name='country_status_create'),
    url(r'^(?i)report/sectorperformance$', views.SectorPerformanceCreate.as_view(), name='sector_performance_create'),    
    url(r'^(?i)report/sectorperformanceedit/(?P<id>[0-9]+)/$', views.SectorPerformanceEdit.as_view(), name='sector_performance_create'),
    url(r'^(?i)report/sectorperformancedelete/(?P<delete>[0-9]+)/$', views.SectorPerformanceDelete.as_view(), name='sector_performance_delete'),    
    url(r'^(?i)report/sectorperformance/list$', views.SectorPerformanceGridView.as_view(), name='sector_performance_create'),    
    url(r'^(?i)report/priorityareaview/list$', views.PriorityAreaView.as_view(), name='Priorityreaview'),    
    
    url(r'^(?i)report/facilityaccess$', views.FacilityAccessCreate.as_view(), name='facility_access_create'),
    url(r'^(?i)report/facilityaccessedit/(?P<id>[0-9]+)/$', views.FacilityAccessEdit.as_view(), name='facility_access_create'),
    url(r'^(?i)report/facilityaccessdelete/(?P<delete>[0-9]+)/$', views.FacilityAccessDelete.as_view(), name='facility_access_delete'),
    url(r'^(?i)report/facilityaccess/list$', views.TechnologyAccessGridView.as_view(), name='facility_access_create'),
    url(r'^(?i)report/planningperformance$', views.PlanningPerformanceCreate.as_view(), name='planning_performance_create'),
    url(r'^(?i)report/planningperformanceedit/(?P<id>[0-9]+)/$', views.PlanningPerformanceEdit.as_view(), name='planning_performance_create'),
    url(r'^(?i)report/planningperformancedelete/(?P<delete>[0-9]+)/$', views.PlanningPerformanceDelete.as_view(), name='planning_performance_delete'),
    url(r'^(?i)report/planningperformance/list$', views.PlanningPerformanceGridView.as_view(), name='planning_performance_create'),
    url(r'^(?i)report/tenderprocperformance$', views.TenderProcedurePerformanceCreate.as_view(), name='tender_proc_performance_create'),
    url(r'^(?i)report/tenderprocperformanceedit/(?P<id>[0-9]+)/$', views.TenderProcedurePerformanceEdit.as_view(), name='tender_proc_performance_create'),
    url(r'^(?i)report/tenderprocperformancedelete/(?P<delete>[0-9]+)/$', views.TenderProcedurePerformanceDelete.as_view(), name='tender_proc_performance_delete'),
    url(r'^(?i)report/tenderprocperformance/list$', views.TPPerformanceGridView.as_view(), name='tender_proc_performance_create'),
    url(r'^(?i)report/communityapproach$', views.CommunityApproachCreate.as_view(), name='community_approach_create'),
    url(r'^(?i)report/communityapproachedit/(?P<id>[0-9]+)/$', views.CommunityApproachEdit.as_view(), name='community_approach_create'),
    url(r'^(?i)report/communityapproachdelete/(?P<delete>[0-9]+)/$', views.CommunityApproachDelete.as_view(), name='community_approach_delete'),
    url(r'^(?i)report/communityapproach/list$', views.CommunityApproachGridView.as_view(), name='community_approach_create'),
    url(r'^(?i)report/partnercontribution$', views.PartnerContributionCreate.as_view(), name='partner_contribution_create'),
    url(r'^(?i)report/partnercontributionedit/(?P<id>[0-9]+)/$', views.PartnerContributionEdit.as_view(), name='partner_contribution_create'),
    url(r'^(?i)report/partnercontributiondelete/(?P<delete>[0-9]+)/$', views.PartnerContributionDelete.as_view(), name='partner_contribution_delete'),
    url(r'^(?i)report/partnercontribution/list$', views.PartnerContributionGridView.as_view(), name='partner_contribution_create'),
    url(r'^(?i)report/partnereventcontribution$', views.PartnerEventContributionCreate.as_view(), name='partner_event_contribution_create'),
    url(r'^(?i)report/partnereventcontributionedit/(?P<id>[0-9]+)/$', views.PartnerEventContributionEdit.as_view(), name='partner_event_contribution_create'),
    url(r'^(?i)report/partnereventcontributiondelete/(?P<delete>[0-9]+)/$', views.PartnerEventContributionDelete.as_view(), name='partner_event_contribution_delete'),
    url(r'^(?i)report/partnereventcontribution/list$', views.PartnerEventContributionGridView.as_view(), name='partner_event_contribution_create'),
    url(r'^(?i)report/swot$', views.SWOTAndConclusionCreate.as_view(), name='swot_create'),
    url(r'^(?i)report/swotedit/(?P<id>[0-9]+)/$', views.SWOTAndConclusionEdit.as_view(), name='swot_create'),
    url(r'^(?i)report/swotdelete/(?P<delete>[0-9]+)/$', views.SWOTAndConclusionDelete.as_view(), name='swot_delete'),
    #Report url
    url(r'^(?i)report/listofpriorityareas$', views.ListofPriorityAreasReport.as_view(), name='list_of_priority_areas_report'),
    url(r'^(?i)report/technologygapperpriorityarea$', views.TechnologyGapPerPriorityAreaReport.as_view(), name='technology_gap_per_priority_area_report'),
    url(r'^(?i)report/technologiesgapsforthecategory$', views.TechnologiesGapsForTheCategory.as_view(), name='technologies_gaps_for_the_category_report'),
    url(r'^(?i)report/estimatedoverallgaps$', views.EstimatedOverallGapsReport.as_view(), name='estimated_overall_gaps_report'),
    #Report To PDF
    url(r'^(?i)report/listofpriorityareasreportpdf$', report_views.ListofPriorityAreasReportToPdf.as_view(), name='list_of_priority_areas_report_to_pdf'),
    url(r'^(?i)report/technologygapclusteredbypa$', report_views.TechnologyGapClusteredByPAReport.as_view(), name='technology_gap_clustered_by_pa_report'),
    url(r'^(?i)report/technologiesgapsforthecategorypdf$', report_views.TechnologiesGapsForTheCategoryReport.as_view(), name='technologiesgaps_for_the_category_report'),
    url(r'^(?i)report/estimatedoverallgapspdf$', report_views.EstimatedOverallGaps.as_view(), name='estimated_overall_gaps'),
    #List to PDF
    url(r'^(?i)report/viewfacilityaccessinpdf$', report_views.view_facilityaccess_in_pdf.as_view(), name='view_facilityaccess_in_pdf'),
    url(r'^(?i)report/viewcomunityapprochinpdf$', report_views.view_comunityapproch_in_pdf.as_view(), name='view_comunityapproch_in_pdf'),
    url(r'^(?i)report/viewcountrydemographicpdf$', report_views.view_countrydemographic_in_pdf.as_view(), name='view_countrydemographic_in_pdf'),
    url(r'^(?i)report/viewpartnercontributionpdf$', report_views.view_partnercontribution_in_pdf.as_view(), name='view_partnercontribution_in_pdf'),
    url(r'^(?i)report/vieweventcontributionpdf$', report_views.view_eventcontribution_in_pdf.as_view(), name='view_eventcontribution_in_pdf'),
    url(r'^(?i)report/viewplanningperformancepdf$', report_views.view_planningperformance_in_pdf.as_view(), name='view_planningperformance_in_pdf'),
    url(r'^(?i)report/viewprioritystatuspdf$', report_views.view_priorityareastatus_in_pdf.as_view(), name='view_priorityareastatus_in_pdf'),
    url(r'^(?i)report/viewsectorperformancepdf$', report_views.view_sectorperformace_in_pdf.as_view(), name='view_sectorperformace_in_pdf'),
    url(r'^(?i)report/viewswotconclusionpdf$', report_views.view_swotconclision_in_pdf.as_view(), name='view_swotconclision_in_pdf'),
    url(r'^(?i)report/viewtenderprocperformancepdf$', report_views.view_tender_proc_performance_in_pdf.as_view(), name='view_tender_proc_performance_in_pdf'),
    #end here
    
    url(r'^(?i)login/$', 'django.contrib.auth.views.login', name='login'),    
    url(r'^(?i)logout/$', views.Logout.as_view(), name='logout'),      
    url(r'^(?i)changepassword/$', views.ChangePassword.as_view(), name='change_password'),
    url(r'^feeds/priority-areas-by-country-id/(\d+)/$', 'dashboard.views.feed_priority_areas'),
    url(r'^feeds/facility-characters-by-sector-category-id/(\d+)/$', 'dashboard.views.feed_facility_characters'),
    url(r'^feeds/technologies-by-facility-character-id/(\d+)/$', 'dashboard.views.feed_technologies'),
    url(r'^feeds/tender-proc-properties-by-sector-category-id/(\d+)/$', 'dashboard.views.feed_tender_proc_properties'),
    url(r'^(?i)$', 'signups.views.home', name='home'),    
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/dashboard/technology/add', views.TechnologyCreate.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)