__author__ = 'savad'
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django_extensions.db import fields

from save_the_change.mixins import SaveTheChange


class TimeStampedBaseModel(SaveTheChange, models.Model):
    """
    An abstract base model that provides self-managed created and
    modified fields.
    """
    created = fields.CreationDateTimeField(verbose_name=_('Created'))
    modified = fields.ModificationDateTimeField(verbose_name=_('Modified'))

    class Meta:
        abstract = True


class GenericBaseModel(TimeStampedBaseModel):
    """
    Base model to create a generic relation
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    relation = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
