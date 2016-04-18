__author__ = 'savad'
from django.conf.urls import patterns, url

from applications.dishes import views

urlpatterns = [
    url(r'^$', views.DishListingView.as_view(), name='dishes'),
]
