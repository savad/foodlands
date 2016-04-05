__author__ = 'savad'
from django.contrib import admin

from applications.activity.feeds.models import Feed


admin.site.register(Feed)
