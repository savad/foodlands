__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.utils.models import GenericBaseModel, TimeStampedBaseModel
from applications.accounts.models import User
from applications.dishes.models import Dish
from applications.foodlands.models import Restaurant


class Image(GenericBaseModel):
    """
    image: required , alternate_text
    Generic model for saving all user uploaded images
    """
    user = models.ForeignKey(User, related_name='user_image', null=True, blank=True)
    image = models.ImageField(_('Image'), )
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    published = models.BooleanField(_('Published?'), default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.content_type)


class RestaurantImages(TimeStampedBaseModel):
    """
    Restaurants images, alternate_text
    Uploaded by Foodlands admin from Django-Admin dashboard
    """
    image = models.ImageField(_('Image'), )
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant_image")
    banner = models.BooleanField(_('Take this image for banner?'), default=False)
    published = models.BooleanField(_('Published?'), default=False)

    def __unicode__(self):
        return self.restaurant.name

    class Meta:
        verbose_name = _('Restaurant Image')
        verbose_name_plural = _('Restaurant Images')


class DishImages(TimeStampedBaseModel):
    """
    Dish images, alternate_text
    Uploaded by Foodlands admin from Django-Admin dashboard
    """
    image = models.ImageField(_('Image'), )
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    dish = models.ForeignKey(Dish, related_name="dish_images")
    banner = models.BooleanField(_('Take this image for banner?'), default=False)
    published = models.BooleanField(_('Published?'), default=False)

    def __unicode__(self):
        return self.dish.name

    class Meta:
        verbose_name = _('Dish Image')
        verbose_name_plural = _('Dish Images')
