from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.entry_list),
    url(r'^entry/new/$', views.entry_new, name='entry_new'),
)
