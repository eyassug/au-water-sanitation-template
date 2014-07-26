from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    
    # Report Urls:
    url(r'^(?i)$', 'signups.views.home', name='home'),    
    url(r'^(?i)report/countrystatus$', 'dashboard.views.create_coutry_status', name='home'),    
    url(r'^(?i)report/facilityaccess$', 'dashboard.views.facility_access', name='facility access'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^(?i)admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)