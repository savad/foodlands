__author__ = 'savad'
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from applications.accounts.models import User


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
        resource_name = 'user'
        authorization = Authorization()
        fields = ["first_name", "last_name", "username", "home_town"]
