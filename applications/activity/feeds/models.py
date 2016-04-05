__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.accounts.models import User
from applications.utils.models import GenericBaseModel


class Feed(GenericBaseModel):
    """
    Model for Saving Activity Feeds
    """
    user = models.ForeignKey(User, verbose_name=_('User'), related_name='get_feed_user')
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    participants = models.ManyToManyField(User, blank=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Feed')
        verbose_name_plural = _('Feed')

    def __unicode__(self):
        return "%s id-%s" %(self.content_type.name, self.object_id)
