__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.utils.models import GenericBaseModel


class Video(GenericBaseModel):
    """
    Model for saving Restaurant video
    link: required, other fields not required
    """
    link = models.CharField(_('Video URL'), max_length=1000)
    image = models.ImageField(_('Thumbnail'), null=True, blank=True, )
    title = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.content_type)
