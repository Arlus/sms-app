from django.conf.urls.defaults import patterns, include, url
from test_app.api import RecordResource
import test_app
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

record_resource = RecordResource()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'payment.views.home', name='home'),
    # url(r'^payment/', include('payment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(record_resource.urls)),
    (r'^incoming/', include('test_app.urls')),
)
