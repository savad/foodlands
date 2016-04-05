__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.utils.models import TimeStampedBaseModel


class Cuisine(TimeStampedBaseModel):
    """
    For style or method of cooking. Eg:Chinese, Arebian
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Cuisine')
        verbose_name_plural = _('Cuisines')


class Serve(TimeStampedBaseModel):
    """
    name: required
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Serve')
        verbose_name_plural = _('Serves')


class Suitable(TimeStampedBaseModel):
    """
    name: required, Suitable for? Eg: Families
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Suitable')
        verbose_name_plural = _('Suitable')


class HighLight(TimeStampedBaseModel):
    """
    Specifying HighLights. Eg: Wifi Available, Parking not available
    """
    name = models.CharField(max_length=100, )
    image = models.ImageField(null=True, blank=True)
    available = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('HighLight')
        verbose_name_plural = _('HighLights')


class Course(TimeStampedBaseModel):
    """
    Course Model, name: required
    """
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __unicode__(self):
        return self.name
