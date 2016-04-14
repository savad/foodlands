__author__ = 'savad'
from django.db import models

from django.utils.translation import ugettext_lazy as _
from applications.accounts.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_delete

from applications.utils.models import GenericBaseModel
from applications.foodlands.models import Restaurant
from applications.activity.feeds.models import Feed


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

    def save(self, *args, **kwargs):
        if not self.pk:
            content_object = self.content_type.model_class().objects.get(id=self.object_id)
            if not self.review_text:
                self.review_type = Review.RATING
            else:
                self.set_expire()
                content_object.review_count += 1
                self.review_type = Review.REVIEW
        super(Review, self).save(*args, **kwargs)

    def set_expire(self):
        qs = Review.objects.filter(object_id=self.object_id, user=self.user, expire=False,
                                   content_type=ContentType.objects.get_for_model(Restaurant))
        content_object = self.content_type.model_class().objects.get(id=self.object_id)
        for review in qs:
            content_object.review_count -= 1
            feed = Feed.objects.get(content_type=ContentType.objects.get_for_model(Review),
                                    object_id=review.id)
            feed.active = False
            feed.save()
        content_object.save()
        qs.update(expire=True)


def update_feed(sender, instance, **kwargs):
    try:
        Feed.objects.get(content_type=ContentType.objects.get_for_model(Review),
                                object_id=instance.id, user=instance.user)
    except Feed.DoesNotExist:
        feed = Feed.objects.create(content_type=ContentType.objects.get_for_model(Review),
                                   object_id=instance.id, user=instance.user)
        feed.save()
post_save.connect(update_feed, sender=Review, dispatch_uid="add_review_to_feed")


def remove_item_from_feed(sender, instance, **kwargs):
    try:
        feed = Feed.objects.get(content_type=ContentType.objects.get_for_model(Review),
                                object_id=instance.id)
        feed.active = False
        feed.save()
    except Feed.ObjectDoesNotExist:
        pass
pre_delete.connect(remove_item_from_feed, sender=Review, dispatch_uid="remove_item_from_feed")
