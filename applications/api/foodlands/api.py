__author__ = 'savad'
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization

from applications.foodlands.models import Restaurant
from applications.api.foodland_specifications.api import CuisineResource, \
    SuitableResource, ServeResource, HighLightResource


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
        "url" : "example.url/restaurant-slug"
    }
    """

    class Meta:
        queryset = Restaurant.objects.all()
        allowed_methods = ['get']
        resource_name = 'foodlands'
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
