from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from applications.location.models import City, Place
from applications.utils.models import TimeStampedBaseModel


class User(AbstractUser, TimeStampedBaseModel):
    """
    User model extends auth.user and stores more user information like city,
    about me, location, activity status etc
    """
    MALE = 'm'
    FEMALE = 'f'
    DEFAULT_GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )
    home_town = models.CharField(_('Home Town'), max_length=100, null=True, blank=True)
    place = models.ForeignKey(Place, verbose_name=_("Place"), null=True, blank=True)
    city = models.ForeignKey(City, verbose_name=_("City"), null=True, blank=True)
    current_city = models.ForeignKey(City, verbose_name=_("Current City"),
                                     related_name="get_current_city", null=True, blank=True)
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=1, choices=DEFAULT_GENDER_CHOICES, default=MALE)
    phone_number = models.CharField(_("Phone Number"), max_length=15, null=True, blank=True)
    about_me = models.TextField(_("About Me"), null=True, blank=True)
    profile_image = models.ImageField(_("Profile Image"), null=True, blank=True)
    cover_image = models.ImageField(_("Cover Image"), null=True, blank=True)

    # fields calculated on the fly to reduce db load
    followers_count = models.IntegerField(_("Followers Count"), default=0)
    following_count = models.IntegerField(_("Following Count"), default=0)
    food_lands_reviewed_count = models.IntegerField(_("Foodland reviewed count"), default=0)
    food_lands_check_in_count = models.IntegerField(_("Foodland check in count"), default=0)
    food_lands_favourite_count = models.IntegerField(_("Foodland favourite count"), default=0)
    food_lands_recommend_count = models.IntegerField(_("Foodland recommend count"), default=0)
    tasted_dishes_count = models.IntegerField(_("Dish tasted count"), default=0)
    favourite_dish_count = models.IntegerField(_("Dish favourite count"), default=0)
    recommend_dish_count = models.IntegerField(_("Dish recommend count"), default=0)
    #user earned points
    point = models.IntegerField(default=0)

    def __unicode__(self):
        if self.first_name:
            return u'%s %s' % (self.first_name, self.last_name)
        return self.username
