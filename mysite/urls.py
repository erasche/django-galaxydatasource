from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('galaxy_datasource.urls', namespace="galaxy_datasource")),
    url(r'^admin/', include(admin.site.urls)),
)
