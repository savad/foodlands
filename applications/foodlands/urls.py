__author__ = 'savad'
from django.conf.urls import patterns, url

from applications.foodlands import views

urlpatterns = [
    url(r'^$', views.FoodlandsView.as_view(), name='foodlands'),
]
