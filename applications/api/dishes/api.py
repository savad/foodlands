__author__ = 'savad'
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization

from applications.dishes.models import Dish
from applications.api.foodland_specifications.api import CuisineResource, CourseResource
from applications.api.foodlands.api import BaseRestaurantResource


class BaseDishResource(ModelResource):
    """
    LIST OF ALL RESTAURANTS
    @outputparams;
     {
        "name" : "fish fry",
        "slug" : "fish-fry",
        "description" : "tasty fish fry",
        "dish_image" : "image.jpg",
        "open_time" : 10:10,
        "close_time" : 8:30,
        "dish_type" : "n"
        "price" : 200
        "restaurant": (F)
        "resource_uri" : "example.url/restaurant-slug"
    }
    """

    class Meta:
        queryset = Dish.objects.all()
        allowed_methods = ['get']
        resource_name = 'dish-list'
        authorization = DjangoAuthorization()
        fields = ["id", "name", "slug", "description", "dish_image", "open_time", "close_time",
                  "dish_type", "price"]


class DishResource(ModelResource):
    """
    LIST OF ALL RESTAURANTS
    @outputparams;
     {
        "id" : 3,
        "name" : "fish fry",
        "slug" : "fish-fry",
        "description" : "tasty fish fry",
        "dish_image" : "image.jpg",
        "price" : 200
        "dish_type" : "n"
        "course" : (F)
        "restaurant": (F)
        "cuisine" : (F)
        "open_time" : 10:10,
        "close_time" : 8:30,
        "food_lands_rating" : 4
        "user_rating": 5
        "tasted_count": 25
        "favourite_count": 35
        "recommend_count": 12
        "comments_count": 356
        "resource_uri" : "example.url/restaurant-slug"
    }
    """
    restaurant = fields.ForeignKey(BaseRestaurantResource, "restaurant", full=True)
    course = fields.ForeignKey(CourseResource, "course", full=True)
    cuisine = fields.ForeignKey(CuisineResource, "cuisine", full=True)

    class Meta:
        queryset = Dish.objects.all()
        allowed_methods = ['get']
        resource_name = 'dish-detail'
        authorization = DjangoAuthorization()
        excludes = ["created", "published", "search_tags"]
