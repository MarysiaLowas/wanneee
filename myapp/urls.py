from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.entry_list),
    url(r'^entry/new/$', views.entry_new, name='entry_new'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tagged_list),
    url(r'^entry/(?P<pk>[0-9]+)/$', views.entry_details),
    url(r'^entry/(?P<pk>[0-9]+)/remove/$', views.entry_remove, name='entry_remove'),
    url(r'^entry/(?P<pk>[0-9]+)/edit/$', views.entry_edit, name='entry_edit'),
)
