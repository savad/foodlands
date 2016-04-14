from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from applications.accounts.models import User


class UserAdmin(UserAdmin):
    list_display = ['__unicode__', 'email', 'city', 'image_thumbnail', 'point']
    readonly_fields = ['followers_count', 'following_count', 'food_lands_reviewed_count',
                       'food_lands_check_in_count', 'food_lands_favourite_count',
                       'food_lands_recommend_count', 'tasted_dishes_count', 'favourite_dish_count',
                       'recommend_dish_count', 'point']
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number',
                                         'place', 'date_of_birth', 'gender', 'city',
                                         'current_city', 'about_me')}),
        (_('Image'), {'fields':('profile_image', 'cover_image')}),
        (_('User Generic Information'), {'fields':('point', 'followers_count',
                                                    'following_count',
                                                    'food_lands_reviewed_count',
                                                    'food_lands_check_in_count',
                                                    'food_lands_favourite_count',
                                                    'food_lands_recommend_count',
                                                    'tasted_dishes_count',
                                                    'favourite_dish_count',
                                                    'recommend_dish_count',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
admin.site.register(User, UserAdmin)
