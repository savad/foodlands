__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from ckeditor.fields import RichTextField

from applications.utils.models import TimeStampedBaseModel
from applications.location.models import City, Place
from applications.foodland_specifications.models import Cuisine, Serve, Suitable, HighLight


class Restaurant(TimeStampedBaseModel):
    """
    Foodlands model
    name, slug, address, city(F), place(F), phone,
    follow_count, recommend, check in_count, etc
    """
    VEG = 'v'
    NON_VEG = 'n'
    TYPE_CHOICE = ((VEG, _('VEG')), (NON_VEG, _('NON-VEG')), )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255, editable=True, unique=True)
    address = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City, verbose_name=_("City"), null=True, blank=True)
    location = models.ForeignKey(Place, verbose_name=_("Place"), null=True, blank=True)
    location_note = models.TextField(max_length=1000, null=True, blank=True)
    lat = models.CharField(_('Latitude'), max_length=100, null=True, blank=True)
    lng = models.CharField(_('Longitude'), max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    small_description = models.TextField(verbose_name=_('Small Description'), null=True, blank=True)
    detailed_describtion = RichTextField(help_text=_('Detailed Description'), null=True, blank=True)
    restaurant_type = models.CharField(_('Restaurant Type'), max_length=1,
                                       choices=TYPE_CHOICE, default=NON_VEG)
    main_image = models.ImageField(_('Main Image '), null=True, blank=True)
    open_time = models.TimeField(_('Open time'), null=True, blank=True)
    close_time = models.TimeField(_('Close time'), null=True, blank=True)
    average_cost = models.IntegerField(_('Average cost'), null=True, blank=True)
    search_tags = models.TextField(_('Search Tags'), null=True, blank=True)
    published = models.BooleanField(_('Published?'), default=False)

    cuisines = models.ManyToManyField(Cuisine, blank=True)
    serves = models.ManyToManyField(Serve, blank=True)
    suitable = models.ManyToManyField(Suitable, blank=True)
    highlights = models.ManyToManyField(HighLight, related_name="get_highlights", blank=True)
    similar_restaurants = models.ManyToManyField('self', blank=True)

    #foodlands admins rating
    foodlands_food_rating = models.DecimalField(_("Food"), default=0, max_digits=2, decimal_places=1)
    foodlands_ambiance_rating = models.DecimalField(_("Ambiance"), default=0, max_digits=2, decimal_places=1)
    foodlands_service_rating = models.DecimalField(_("Service"), default=0, max_digits=2, decimal_places=1)

    # Dynamically changes the fields.
    dishes_count = models.IntegerField(_("Dishes Count"), default=0)
    favourite_count = models.IntegerField(_("Favourite Count"), default=0)
    follow_count = models.IntegerField(_("Follow Count"), default=0)
    recommend_count = models.IntegerField(_("Recommends Count"), default=0)
    review_count = models.IntegerField(_("Review Count"), default=0)
    check_in_count = models.IntegerField(_("Check in Count"), default=0)
    user_food_rating = models.DecimalField(_("User food rating"), default=0, max_digits=2, decimal_places=1)
    user_ambiance_rating = models.DecimalField(_("User amb rating"), default=0, max_digits=2, decimal_places=1)
    user_service_rating = models.DecimalField(_("User service rating"), default=0, max_digits=2, decimal_places=1)

    #SEO fields
    seo_title = models.CharField(_('Title'), max_length=255, null=True, blank=True)
    seo_description = models.TextField(_('Description'), null=True, blank=True)
    seo_keywords = models.TextField(_('Keywords'), null=True, blank=True)
    seo_image = models.ImageField(_('SEO Image'), null=True, blank=True)

    def __unicode__(self):
        if self.city:
            return '%s, %s' % (self.name, self.city.name)
        return self.name

    class Meta:
        verbose_name = _('Foodland')
        verbose_name_plural = _('Foodlands')
