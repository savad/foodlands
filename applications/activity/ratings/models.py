__author__ = 'savad'
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from applications.accounts.models import User
from applications.utils.models import GenericBaseModel
from applications.activity.feeds.models import Feed


class Rating(GenericBaseModel):
    """
    Saving Dishes  Ratings details
    """
    user = models.ForeignKey(User, verbose_name=_('User'))
    rating = models.PositiveIntegerField(_("Rating"))

    def __unicode__(self):
        return u'%s' % self.user.username

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')


def update_feed(sender, instance, **kwargs):
    feed = Feed.objects.create(content_type=ContentType.objects.get_for_model(Rating),
                               object_id=instance.id, user=instance.user)
    feed.save()
post_save.connect(update_feed, sender=Rating, dispatch_uid="update_feed")


def remove_item_from_feed(sender, instance, **kwargs):
    try:
        feed = Feed.objects.get(content_type=ContentType.objects.get_for_model(Rating),
                                object_id=instance.id)
        feed.active = False
        feed.save()
    except Feed.ObjectDoesNotExist:
        pass
pre_delete.connect(remove_item_from_feed, sender=Rating, dispatch_uid="remove_from_feed")
