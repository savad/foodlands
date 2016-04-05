__author__ = 'savad'
from django.db import models

from django.utils.translation import ugettext_lazy as _
from applications.accounts.models import User

from applications.utils.models import GenericBaseModel


class Review(GenericBaseModel):
    """
    Saving Restaurants Review details
    """
    COMMENT = 'c'
    RATING = 'rt'
    REVIEW = 'rw'
    TYPE_CHOICE = ((COMMENT, _('COMMENT')), (RATING, _('RATING')), (REVIEW, _('REVIEW')), )

    user = models.ForeignKey(User, verbose_name=_('User'), related_name="get_review_user")
    review_text = models.TextField(null=True, blank=True)
    food_rating = models.DecimalField(_("Food rating"), default=0,
                                      max_digits=2, decimal_places=1)
    ambiance_rating = models.DecimalField(_("Ambiance rating"), default=0,
                                          max_digits=2, decimal_places=1)
    service_rating = models.DecimalField(_("service rating"), default=0,
                                         max_digits=2,decimal_places=1)
    review_type = models.CharField(_('Review Type'), max_length=2,
                                   choices=TYPE_CHOICE, default=REVIEW)
    expire = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' %(self.user.username)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
