__author__ = 'savad'
from django.contrib import admin
from django.utils.translation import ugettext as _

from applications.foodlands.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('dishes_count', 'favourite_count', 'follow_count', 'recommend_count',
                       'review_count', 'check_in_count', 'user_food_rating',
                       'user_ambiance_rating', 'user_service_rating')

    fieldsets = (
        ("General Information", {'fields': ('name', 'slug', 'address', 'city', 'location',
                                            'phone', 'average_cost', 'restaurant_type',
                                            'published')}),
        (_('Description'), {'fields': ('small_description', 'detailed_description', )}),
        (_('FoodLands Rating'), {'fields': ('foodlands_food_rating',
                                            'foodlands_ambiance_rating',
                                            'foodlands_service_rating',)}),
        (_('Timings'), {'fields': ('open_time', 'close_time')}),
        (_('FoodLands Images'), {'fields': ('main_image', )}),
        (_('Location Info'), {'fields': ('location_note', 'lat', 'lng', )}),
        (_('Other Info'), {'fields': ('cuisines', 'suitable', 'serves', 'highlights')}),
        (_('Similar Restaurants'), {'fields': ('similar_restaurants', )}),
        (_('Status Report'), {'fields': ('favourite_count', 'follow_count', 'recommend_count',
                                         'review_count', 'check_in_count', 'user_food_rating',
                                         'user_ambiance_rating', 'user_service_rating')}),
        (_('Search Tag'), {'fields': ('search_tags', )}),
        (_('SEO'), {'fields': ('seo_title', 'seo_description', 'seo_keywords', 'seo_image' )}),

    )

    filter_horizontal = ('similar_restaurants', 'cuisines', 'suitable', 'serves', 'highlights')
    list_display = ('name', 'city', 'follow_count', 'restaurant_type',)
    list_filter = ('city', 'restaurant_type')
    search_fields = ('name', 'city', 'small_description', 'detailed_description')
    ordering = ('name', )
admin.site.register(Restaurant, RestaurantAdmin)
