__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from timezone_field import TimeZoneField

from applications.utils.models import TimeStampedBaseModel


class Country(TimeStampedBaseModel):
    """
    Country model. field: name required
    """
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class State(TimeStampedBaseModel):
    """
    State Model. fields: name, country, slug
    All fields are required
    """
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', max_length=255, editable=True, unique=True)
    country = models.ForeignKey(Country, verbose_name="Country", )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


class City(TimeStampedBaseModel):
    """
    City Model. Fields name, state, country, timezone, slug
    All fields are required
    """
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', max_length=255, editable=True, unique=True)
    state = models.ForeignKey(State, verbose_name="State")
    country = models.ForeignKey(Country, verbose_name="Country")
    timezone = TimeZoneField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

class Place(TimeStampedBaseModel):
    """
    Place Model. Fields name and city
    All fields are required
    """
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, verbose_name="city")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
