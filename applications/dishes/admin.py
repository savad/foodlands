__author__ = 'savad'
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from applications.dishes.models import Dish


class DishAdmin(admin.ModelAdmin):
    readonly_fields = ('user_rating', 'tasted_count', 'favourite_count', 'recommend_count',
                       'comments_count')
    fieldsets = [
        ("General Information", {'fields': ('name', 'description', 'foodlands_rating', 'price',
                                            'dish_type', 'course', 'cuisine', 'restaurant',
                                            'published')}),
        (_('Timings'), {'fields': ('open_time', 'close_time')}),
        (_('Dish Images'), {'fields': ('dish_image', )}),
        (_('Status Report'), {'fields': ('tasted_count', 'favourite_count', 'recommend_count',
                                         'comments_count')}),
        (_('Search Tag'), {'fields': ('search_tags', )}),
        (_('SEO'), {'fields': ('seo_title', 'seo_description', 'seo_keywords', 'seo_image' )}),

    ]
    list_display = ('__unicode__', 'foodlands_rating', 'tasted_count', 'price',
                    'open_time', 'close_time')
    list_filter = ('dish_type', 'price', 'foodlands_rating')
    search_fields = ('name', 'price', 'description', 'restaurant__name')
admin.site.register(Dish, DishAdmin)
