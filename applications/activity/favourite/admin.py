__author__ = 'savad'
from django.contrib import admin

from applications.activity.favourite.models import Favourite


admin.site.register(Favourite)
