__author__ = 'savad'
from django.db import models

from django.utils.translation import ugettext_lazy as _
from applications.accounts.models import User

from applications.utils.models import TimeStampedBaseModel


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
