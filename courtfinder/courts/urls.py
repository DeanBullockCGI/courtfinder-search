from django.conf.urls import patterns, url
from courts import views

urlpatterns = patterns('',
	url(r'^(?P<slug>.+)/leaflet/(?P<leaflet_type>.+)$', views.leaflet, name='leaflet'),
    url(r'^(?P<first_letter>[A-Z])?$', views.list, name='list'),
    url(r'^(?P<slug>.+)$', views.court, name='court'),  
)

