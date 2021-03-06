__author__ = 'savad'
from django.db import models

from django.utils.translation import ugettext_lazy as _
from applications.accounts.models import User

from applications.utils.models import GenericBaseModel


class Comment(GenericBaseModel):
    """
    Saving Restaurants, Feed and Dish Comments
    """
    user = models.ForeignKey(User, verbose_name=_('User'))
    text = models.TextField()

    def __unicode__(self):
        return u'%s' %(self.user.username)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
