__author__ = 'savad'
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import FormValidation

from applications.dishes.models import Dish
from applications.api.foodland_specifications.api import CuisineResource, CourseResource
from applications.api.foodlands.api import BaseRestaurantResource
from applications.api.utils import GenericCreateMixin, BaseMeta
from applications.activity.favourite.models import Favourite
from applications.activity.follow.models import Follow
from applications.activity.recommend.models import Recommend
from applications.activity.tasted.models import Tasted
from applications.activity.ratings.models import Rating
from applications.activity.favourite.forms import FavouriteForm
from applications.activity.follow.forms import FollowForm
from applications.activity.recommend.forms import RecommendForm
from applications.activity.tasted.forms import TastedForm
from applications.activity.ratings.forms import RatingForm


class BaseDishResource(ModelResource):
    """
    LIST OF ALL Dishes
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
    LIST OF ALL DISHES
    @output params;
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


class DishFavouriteResource(GenericCreateMixin, ModelResource):
    """
    Favourite AND Remove Favourite Dish
    @input params;
    {
    "object_id:36"
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36,
    }
    """
    model = Favourite
    generic_model = Dish

    class Meta(BaseMeta):
        queryset = Favourite.objects.all()
        resource_name = 'dish-favourite'
        validation = FormValidation(form_class=FavouriteForm)
        fields = ["id", "object_id"]


class DishFollowResource(GenericCreateMixin, ModelResource):
    """
    Follow AND Un-Follow Dish
    @input params;
    {
    "object_id:36"
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36,
    }
    """
    model = Follow
    generic_model = Dish

    class Meta(BaseMeta):
        queryset = Follow.objects.all()
        resource_name = 'dish-follow'
        validation = FormValidation(form_class=FollowForm)
        fields = ["id", "object_id"]


class DishRecommendResource(GenericCreateMixin, ModelResource):
    """
    Recommend AND Remove Recommend Dish
    @input params;
    {
    "object_id:36"
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36,
    }
    """
    model = Recommend
    generic_model = Dish

    class Meta(BaseMeta):
        queryset = Recommend.objects.all()
        resource_name = 'dish-recommend'
        validation = FormValidation(form_class=RecommendForm)
        fields = ["id", "object_id"]


class DishTastedResource(GenericCreateMixin, ModelResource):
    """
    Tasted AND Remove Tasted Dish
    @input params;
    {
    "object_id:36"
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36,
    }
    """
    model = Tasted
    generic_model = Dish

    class Meta(BaseMeta):
        queryset = Tasted.objects.all()
        resource_name = 'dish-tasted'
        validation = FormValidation(form_class=TastedForm)
        fields = ["id", "object_id"]


class DishRatingResource(GenericCreateMixin, ModelResource):
    """
    Tasted AND Remove Tasted Dish
    @input params;
    {
    "object_id:36"
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36,
    }
    """
    model = Rating
    generic_model = Dish

    class Meta(BaseMeta):
        queryset = Rating.objects.all()
        resource_name = 'dish-rating'
        validation = FormValidation(form_class=RatingForm)
        fields = ["id", "object_id", "rating"]
