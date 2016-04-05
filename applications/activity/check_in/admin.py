__author__ = 'savad'
from django.contrib import admin

from applications.activity.check_in.models import CheckIn


admin.site.register(CheckIn)
