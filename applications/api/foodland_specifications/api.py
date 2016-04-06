__author__ = 'savad'
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization

from applications.foodland_specifications.models import Course, Cuisine, Serve, Suitable, HighLight


class CuisineResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Dinner",
    }
    """

    class Meta:
        queryset = Cuisine.objects.all()
        allowed_methods = ['get']
        resource_name = 'cuisine'
        authorization = DjangoAuthorization()
        fields = ["id", "name"]


class CourseResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Veg",
    }
    """

    class Meta:
        queryset = Course.objects.all()
        allowed_methods = ['get']
        resource_name = 'course'
        authorization = DjangoAuthorization()
        fields = ["id", "name"]


class ServeResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Family",
    }
    """

    class Meta:
        queryset = Serve.objects.all()
        allowed_methods = ['get']
        resource_name = 'serve'
        authorization = DjangoAuthorization()
        fields = ["id", "name"]


class SuitableResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Family",
    }
    """

    class Meta:
        queryset = Suitable.objects.all()
        allowed_methods = ['get']
        resource_name = 'suitable'
        authorization = DjangoAuthorization()
        fields = ["id", "name"]


class HighLightResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Wifi",
        "available" : "True",
        "image" : "image.jpg",
    }
    """
    class Meta:
        queryset = HighLight.objects.all()
        allowed_methods = ['get']
        resource_name = 'highlight'
        authorization = DjangoAuthorization()
        fields = ["id", "name", "image", "available"]
