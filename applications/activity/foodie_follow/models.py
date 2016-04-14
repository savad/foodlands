__author__ = 'savad'
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from applications.accounts.models import User
from applications.utils.models import TimeStampedBaseModel
from applications.activity.feeds.models import Feed


class FoodieFollow(TimeStampedBaseModel):
    """
    Saving Foodies Follow details
    """
    following = models.ForeignKey(User, verbose_name=_('Following'), related_name="foodie_followings")
    follower = models.ForeignKey(User, verbose_name=_('Follower'), related_name='foodie_followers')

    def __unicode__(self):
        return self.follower.first_name

    class Meta:
        verbose_name = _('Foodies Follow')
        verbose_name_plural = _('Foodies Follow')


def update_feed(sender, instance, **kwargs):
    feed = Feed.objects.create(content_type=ContentType.objects.get_for_model(FoodieFollow),
                               object_id=instance.id, user=instance.user)
    feed.save()
post_save.connect(update_feed, sender=FoodieFollow, dispatch_uid="update_feed")


def remove_item_from_feed(sender, instance, **kwargs):
    try:
        feed = Feed.objects.get(content_type=ContentType.objects.get_for_model(FoodieFollow),
                                object_id=instance.id)
        feed.active = False
        feed.save()
    except Feed.ObjectDoesNotExist:
        pass
pre_delete.connect(remove_item_from_feed, sender=FoodieFollow, dispatch_uid="remove_from_feed")
