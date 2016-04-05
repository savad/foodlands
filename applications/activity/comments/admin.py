__author__ = 'savad'
from django.contrib import admin

from applications.activity.comments.models import Comment


admin.site.register(Comment)
