__author__ = 'savad'
from django.contrib import admin

from applications.location.models import Place, City, State, Country


admin.site.register(Place)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
