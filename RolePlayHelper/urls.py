from django.conf.urls import patterns, include, url
from django.contrib import admin
import equipment

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^', include("equipment.urls")),
)
