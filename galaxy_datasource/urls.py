from django.conf.urls import patterns, url

from galaxy_datasource import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.data, name='data'),
)
