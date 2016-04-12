__author__ = 'savad'
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import FormValidation
from tastypie.authentication import BasicAuthentication,\
    SessionAuthentication, MultiAuthentication, ApiKeyAuthentication

from applications.foodlands.models import Restaurant
from applications.activity.follow.models import Follow
from applications.activity.follow.forms import FollowForm
from applications.api.foodland_specifications.api import CuisineResource, \
    SuitableResource, ServeResource, HighLightResource
from applications.api.accounts.api import UserResource
from applications.api.utils import GenericCreateMixin


class BaseRestaurantResource(ModelResource):
    """
    LIST OF ALL RESTAURANTS
    @outputparams;
     {
        "name" : "Taj",
        "slug" : "taj",
        "address" : "Taj tower,Calicut",
        "city" : "Calicut",
        "phone" : "1234566",
        "small_description" : "Lorem Ipsum",
        "restaurant_type" : "n"
        "open_time" : 10:10,
        "close_time" : 8:30,
        "main_image" : "image.jpg"
        "average_cost" : 20
        "resource_uri" : "example.url/restaurant-slug"
    }
    """
    class Meta:
        queryset = Restaurant.objects.all()
        allowed_methods = ['get']
        resource_name = 'food-lands-list'
        authorization = DjangoAuthorization()
        fields = ["id", "name", "slug", "address", "city", "phone", "small_description",
                  "restaurant_type", "open_time", "close_time", "main_image", "url"]


class RestaurantResource(ModelResource):
    """
    LIST OF ALL RESTAURANTS
    @outputparams;
     {
        "name" : "Taj",
        "slug" : "taj",
        "address" : "Taj tower,Calicut",
        "city" : "Calicut",
        "location" : "Mananchira",
        "location_note" : "Mananchira opp bus stand",
        "lat" : 0.024
        "lng" : 0.568
        "phone" : "1234566",
        "small_description" : "Lorem Ipsum",
        "restaurant_type" : "n"
        "main_image" : "image.jpg"
        "open_time" : 10:10,
        "close_time" : 8:30,
        "average_cost" : 20
        "resource_uri" : "example.url/restaurant-slug"
        "cuisines" : veg
        "serves" : lunch
        "suitable": family
        "highlights" : [wifi, parking]
        "similar_restaurants" : []
        "foodlands_food_rating" : 3
        "foodlands_ambiance_rating" : 3
        "foodlands_service_rating" : 3
        "dishes_count" : 7
        "favourite_count" : 7
        "follow_count" : 7
        "recommend_count" : 7
        "review_count" : 7
        "check_in_count" : 7
        "user_food_rating" : 4
        "user_ambiance_rating" : 4
        "user_service_rating" : 4
        "seo_title" : "Taj Hotel"
        "seo_description" : "Hotel desc"
        "seo_keywords" : "Hotel, Fish Fry"
        "seo_image" : "image.jpg"
    }
    """
    city = fields.CharField(attribute="city")
    location = fields.CharField(attribute="location")
    cuisines = fields.ToManyField(CuisineResource, "cuisines", full=True)
    serves = fields.ToManyField(ServeResource, "serves", full=True)
    suitable = fields.ToManyField(SuitableResource, "suitable", full=True)
    highlights = fields.ToManyField(HighLightResource, "highlights", full=True)
    similar_restaurants = fields.ToManyField(BaseRestaurantResource,
                                             "similar_restaurants", full=True)

    class Meta:
        queryset = Restaurant.objects.all()
        allowed_methods = ['get']
        resource_name = 'foodlands-detail'
        authorization = DjangoAuthorization()
        excludes = ["created", "published", "search_tags"]


class RestaurantFollowResource(GenericCreateMixin, ModelResource):
    """
    FOLLOW AND UN-FOLLOW RESTAURANT
    @inputparams;
    {
    "object_id:36"
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @outputparams;
    {
    "content_type": "Foodland",
    "id": 15,
    "object_id": 1,
    "resource_uri": "/api/v1/food-land-follow/15/",
    "user": {
        "first_name": "Tom",
        "home_town": "Cochin",
        "last_name": "KP",
        "resource_uri": "",
        "username": "tom"
        }
    }
    """
    content_type = fields.CharField(attribute='content_type')
    user = fields.ForeignKey(UserResource, 'user', full=True)
    model = Follow
    generic_model = Restaurant

    class Meta:
        queryset = Follow.objects.all()
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        resource_name = 'food-land-follow'
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(),
                                             ApiKeyAuthentication())
        form = FormValidation(form_class=FollowForm)
        always_return_data = True
        fields = ["id", "object_id"]
