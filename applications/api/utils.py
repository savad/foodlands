__author__ = 'savad'
import ast

from django.contrib.contenttypes.models import ContentType

from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication,\
    SessionAuthentication, MultiAuthentication, ApiKeyAuthentication


class ContentTypeResource(ModelResource):
    """
    @outputparams;
     {
        "app_label" : "foodlands",
        "model" : "Restaurant",
        "objects" : "17"
    }
    """
    class Meta:
        queryset = ContentType.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'content-type'
        authorization = DjangoAuthorization()


class GenericCreateMixin(object):
    """
    This class check whether the instance is exist or not.
    If exist then return that instance.
    Else create new instance.
    """

    def obj_create(self, bundle, **kwargs):
        data = ast.literal_eval(bundle.request.body)
        bundle.obj = self._meta.object_class()
        object_id = data.get('object_id')
        instance = self.get_activity_instance(object_id, bundle.request.user)
        kwargs["user"] = bundle.request.user
        kwargs["content_type"] = ContentType.objects.get_for_model(self.generic_model)
        if instance:
            kwargs["id"], kwargs["pk"] = instance.id, instance.id
        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)
        bundle = self.full_hydrate(bundle)
        if not instance:
            return self.save(bundle)
        return bundle

    def get_activity_instance(self, object_id, user):
        content_type = ContentType.objects.get_for_model(self.generic_model)
        try:
            content_object = self.model.objects.get(content_type=content_type,
                                                    object_id=object_id, user=user)
            return content_object
        except self.model.DoesNotExist:
            return None


class BaseMeta:
    allowed_methods = ['get', 'post']
    list_allowed_methods = ['get', 'post']
    detail_allowed_methods = ['get', 'put', 'delete']
    always_return_data = True
    include_resource_uri = False
    authorization = DjangoAuthorization()
    authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(),
                                         ApiKeyAuthentication())
