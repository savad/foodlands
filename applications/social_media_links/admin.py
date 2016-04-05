__author__ = 'savad'
from django.contrib import admin

from applications.social_media_links.models import SocialMedialLinks

class SocialLinksAdmin(admin.ModelAdmin):
    """
    Social medias admin
    """
    list_display = ['title', 'sort_order', 'display', 'targt']
    list_editable = ['sort_order', 'display', 'targt']
    search_fields = ('title', 'link', 'targt')
    list_filter = ('targt', )

admin.site.register(SocialMedialLinks, SocialLinksAdmin)
