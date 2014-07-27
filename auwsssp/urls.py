from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from dashboard import views

urlpatterns = patterns('',
    # Home:
    
    # Report Urls:
    url(r'^(?i)report/countrystatus$', views.CountryStatusCreate.as_view(), name='country_status_create'),
    url(r'^(?i)report/sectorperformance$', views.SectorPerformanceCreate.as_view(), name='sector_performance_create'),    
    url(r'^(?i)report/facilityaccess$', views.FacilityAccessCreate.as_view(), name='facility_access_create'),
    url(r'^(?i)report/planningperformance$', views.PlanningPerformanceCreate.as_view(), name='planning_performance_create'),
    url(r'^(?i)report/tenderprocperformance$', views.TenderProcedurePerformanceCreate.as_view(), name='tender_proc_performance_create'),
    url(r'^(?i)report/communityapproach$', views.CommunityApproachCreate.as_view(), name='community_approach_create'),
    url(r'^(?i)report/partnercontribution$', views.PartnerContributionCreate.as_view(), name='partner_contribution_create'),
    url(r'^(?i)report/partnereventcontribution$', views.PartnerEventContributionCreate.as_view(), name='partner_event_contribution_create'),
    url(r'^(?i)report/swot$', views.SWOTAndConclusionCreate.as_view(), name='swot_create'),
    url(r'^(?i)login/$', 'django.contrib.auth.views.login', name='login'),    
    url(r'^(?i)logout/$', views.Logout.as_view(), name='logout'),

    url(r'^(?i)$', 'signups.views.home', name='home'),    
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)