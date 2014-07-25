from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from dashboard import views

urlpatterns = patterns('',
    # Home:
    
    # Report Urls:
    url(r'^report/countrystatus$', views.CountryStatusCreate.as_view(), name='country_status_create'),
    url(r'^report/sectorperformance$', views.SectorPerformanceCreate.as_view(), name='sector_performance_create'),    
    url(r'^report/facilityaccess$', views.FacilityAccessCreate.as_view(), name='facility_access_create'),
    url(r'^report/planningperformance$', views.PlanningPerformanceCreate.as_view(), name='planning_performance_create'),
    url(r'^report/tenderprocperformance$', views.TenderProcedurePerformanceCreate.as_view(), name='tender_proc_performance_create'),
    url(r'^report/communityapproach$', views.CommunityApproachCreate.as_view(), name='community_approach_create'),
    url(r'^report/partnercontribution$', views.PartnerContributionCreate.as_view(), name='partner_contribution_create'),
    url(r'^report/partnereventcontribution$', views.PartnerEventContributionCreate.as_view(), name='partner_event_contribution_create'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)