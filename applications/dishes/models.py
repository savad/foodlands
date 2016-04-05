__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField

from applications.utils.models import TimeStampedBaseModel
from applications.foodland_specifications.models import Cuisine, Course
from applications.foodlands.models import Restaurant


class Dish(TimeStampedBaseModel):
    """
    Dish Model
    name, description, price, open time, restaurant(F),
    rating, tasted_count, favorite_count, cuisine,
    veg, comments_count , etc
    """
    VEG = 'v'
    NON_VEG = 'n'
    TYPE_CHOICE = ((VEG, _('VEG')), (NON_VEG, _('NON-VEG')), )
    name = models.CharField(_('Dish Name'), max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255, editable=False, unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    dish_image = models.ImageField(_('Dish Image '), null=True, blank=True)
    price = models.FloatField(_('Price'), default=0, help_text=_("Price of the Dish"))
    dish_type = models.CharField(_('Dish Type'), max_length=1, choices=TYPE_CHOICE, default='n')
    course = models.ForeignKey(Course, verbose_name='course', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    cuisine = models.ForeignKey(Cuisine, related_name='get_cuisine', null=True, blank=True)
    open_time = models.TimeField(_('Open time'), null=True, blank=True)
    close_time = models.TimeField(_('Close time'), null=True, blank=True)
    foodlands_rating = models.FloatField(_('Rating'), default=0, db_index=True)
    search_tags = models.TextField(_('Search Tags'), null=True, blank=True)
    published = models.BooleanField(_('Published?'), default=True)

    #Dynamically update the fields
    user_rating = models.FloatField(_('Rating'), default=0, db_index=True)
    tasted_count = models.PositiveIntegerField(_('Tasted Count'), default=0)
    favourite_count = models.PositiveIntegerField(_('Favourite Count'), default=0)
    recommend_count = models.PositiveIntegerField(_('Bookmark Count'), default=0)
    comments_count = models.PositiveIntegerField(_('Comments Count'), default=0)

    #SEO fields
    seo_title = models.CharField(_('Title'), max_length=255, null=True, blank=True)
    seo_description = models.TextField(_('Description'), null=True, blank=True)
    seo_keywords = models.TextField(_('Keywords'), null=True, blank=True)
    seo_image = models.ImageField(_('SEO Image'),  null=True, blank=True)


    class Meta:
        verbose_name = _('Dish')
        verbose_name_plural = _('Dishes')

    def __unicode__(self):
        if self.restaurant and self.restaurant.city:
            return '%s, %s, %s' % (self.name, self.restaurant.name, self.restaurant.city.name)
        elif self.restaurant:
            return '%s, %s' % (self.name, self.restaurant.name)
        return self.name
