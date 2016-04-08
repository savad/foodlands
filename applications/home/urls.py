__author__ = 'savad'
from django.conf.urls import patterns, url

from applications.home import views

urlpatterns = patterns('',
                       url(r'^$', views.HomePageView.as_view(), name='home'),
                       )
