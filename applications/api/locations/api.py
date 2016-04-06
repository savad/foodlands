__author__ = 'savad'
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization

from applications.location.models import Place, City, State, Country


class CountryResource(ModelResource):
    """
    List of all Country
    @outputparams;
     {
        "id" : 1,
        "name" : "India",
        "country_code" : "IN"
    }
    """

    class Meta:
        queryset = Country.objects.all()
        allowed_methods = ['get']
        resource_name = 'country'
        authorization = DjangoAuthorization()
        fields = ["id", "name", "country_code"]



class StateResource(ModelResource):
    """
    List of all States
    @outputparams;
     {
        "id" : 1,
        "name" : "Kerala",
        "slug" : "kerala",
        "country" : [{"name": "India", "id": 1}]
    }
    """
    country = fields.ForeignKey(CountryResource, 'country', full=True)
    class Meta:
        queryset = State.objects.all()
        allowed_methods = ['get']
        resource_name = 'state'
        authorization = DjangoAuthorization()
        fields = ["id", "slug", "name"]


class CityResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Kochi",
        "slug" : "kochi",
        "state" : (F),
        "country" : (F),
    }
    """
    country = fields.ForeignKey(CountryResource, 'country', full=True)
    state = fields.ForeignKey(StateResource, 'state', full=True)
    class Meta:
        queryset = City.objects.all()
        allowed_methods = ['get']
        resource_name = 'city'
        authorization = DjangoAuthorization()
        fields = ["id", "name", "slug", "timezone"]


class PlaceResource(ModelResource):
    """
    List of all Cuisine
    @outputparams;
     {
        "id" : 1,
        "name" : "Kakkanadu",
        "city": (F)
    }
    """
    city = fields.ForeignKey(CityResource, 'city', full=True)
    class Meta:
        queryset = Place.objects.all()
        allowed_methods = ['get']
        resource_name = 'place'
        authorization = DjangoAuthorization()
        fields = ["id", "name"]
