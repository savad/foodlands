__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.utils.models import TimeStampedBaseModel


class SocialMedialLinks(TimeStampedBaseModel):
    """
    Model for saving social links like facebook,google, twitter etc.
    """
    TARGET = (('_blank', 'Blank'), ('_top', 'Top'))
    TITLE_FIELDS = (
        ('facebook', _('Facebook')),
        ('twitter', _('Twitter')),
        ('google', _('Google+')),
        ('instagram', _('Instagram')),
        ('linkedin', _('Linkedin')),
        ('youtube', _('Youtube')),
        ('pinterest', _('Pinterest')),)

    title = models.CharField(_("Title"), max_length=150, choices=TITLE_FIELDS)
    link = models.CharField(verbose_name=_('Link'),max_length=300, )
    targt = models.CharField(_("Target"), choices=TARGET, default='_blank', max_length=6)
    sort_order = models.IntegerField(_("Sort order"), default=0)
    display = models.BooleanField(_("Publish"), default=True)

    class Meta:
        verbose_name = _("Social Media Link")
        verbose_name_plural = _("Social Media Links")
        ordering = ('sort_order', )

    def __unicode__(self):
        return "%s" % self.title
