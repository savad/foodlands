__author__ = 'savad'
from django.conf.urls import patterns, include, url

from tastypie.api import Api

from api.accounts import api as account_api

v1_api = Api(api_name='v1')
v1_api.register(account_api.UserResource())

