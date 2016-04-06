__author__ = 'savad'
from django.contrib import admin

from applications.foodland_specifications.models import Suitable, Serve, Cuisine, Course, HighLight


admin.site.register(Suitable)
admin.site.register(Serve)
admin.site.register(Cuisine)
admin.site.register(Course)
admin.site.register(HighLight)
