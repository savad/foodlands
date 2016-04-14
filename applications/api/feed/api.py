__author__ = 'savad'
from django.contrib.contenttypes.models import ContentType

from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from applications.api.utils import BaseMeta
from applications.api.utils import GenericCreateMixin
from applications.activity.likes.forms import LikeForm
from applications.activity.comments.forms import CommentForm
from applications.activity.likes.models import Like
from applications.activity.comments.models import Comment
from applications.activity.feeds.models import Feed


class FeedLikeResource(GenericCreateMixin, ModelResource):
    """
    Feed Like API
    @input params;
    {
    "object_id": 36,
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36
    }
    """
    model = Like
    generic_model = Feed

    class Meta(BaseMeta):
        queryset = Like.objects.all()
        resource_name = 'feed-like'
        validation = FormValidation(form_class=LikeForm)
        fields = ["id", "object_id"]


class FeedCommentLikeResource(GenericCreateMixin, ModelResource):
    """
    Feed Comment Like API
    @input params;
    {
    "object_id": 36,
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36
    }
    """
    model = Like
    generic_model = Comment

    class Meta(BaseMeta):
        queryset = Like.objects.all()
        resource_name = 'feed-comment-like'
        validation = FormValidation(form_class=LikeForm)
        fields = ["id", "object_id"]


class FeedCommentResource(ModelResource):
    """
    Feed Comment API
    @input params;
    {
    "object_id": 36,
    "text": "Good One",
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36
    "text": "Good One"
    }
    """

    class Meta(BaseMeta):
        queryset = Comment.objects.all()
        resource_name = 'feed-comment'
        validation = FormValidation(form_class=CommentForm)
        fields = ["id", "object_id", "text"]

    def obj_create(self, bundle, **kwargs):
        bundle.obj = self._meta.object_class()
        kwargs["user"] = bundle.request.user
        kwargs["content_type"] = ContentType.objects.get_for_model(Feed)
        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)
        bundle = self.full_hydrate(bundle)
        return self.save(bundle)
