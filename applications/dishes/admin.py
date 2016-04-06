__author__ = 'savad'
from django.contrib import admin

from applications.dishes.models import Dish


admin.site.register(Dish)
