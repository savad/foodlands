__author__ = 'savad'
import ast

from django.contrib.contenttypes.models import ContentType

from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import FormValidation
from tastypie.authentication import BasicAuthentication,\
    SessionAuthentication, MultiAuthentication, ApiKeyAuthentication

from applications.foodlands.models import Restaurant
from applications.activity.follow.models import Follow
from applications.activity.check_in.models import CheckIn
from applications.activity.recommend.models import Recommend
from applications.activity.favourite.models import Favourite
from applications.activity.review.models import Review
from applications.activity.follow.forms import FollowForm
from applications.activity.check_in.forms import CheckInForm
from applications.activity.favourite.forms import FavouriteForm
from applications.activity.recommend.forms import RecommendForm
from applications.activity.review.forms import ReviewForm
from applications.api.foodland_specifications.api import CuisineResource, \
    SuitableResource, ServeResource, HighLightResource
from applications.api.utils import GenericCreateMixin


class BaseRestaurantResource(ModelResource):
    """
    LIST OF ALL RESTAURANTS
    @output params;
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
        "average_rating" : 2.6,
        "follow_count" : 254,
        "recommend_count" : 365,
        "favourite_count" : 652
    }
    """
    class Meta:
        queryset = Restaurant.objects.all()
        allowed_methods = ['get']
        resource_name = 'food-lands-list'
        authorization = DjangoAuthorization()
        fields = ["id", "name", "slug", "address", "city", "phone", "small_description",
                  "restaurant_type", "open_time", "close_time", "main_image", "url",
                  "follow_count", "recommend_count", "favourite_count"]

    def dehydrate(self, bundle):
        bundle.data['average_rating'] = (bundle.obj.foodlands_food_rating + bundle.obj.foodlands_ambiance_rating
                                         + bundle.obj.foodlands_service_rating)/3
        return bundle


class RestaurantResource(ModelResource):
    """
    LIST OF ALL RESTAURANTS
    @output params;
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
        validation = FormValidation(form_class=FollowForm)
        always_return_data = True
        include_resource_uri = False
        fields = ["id", "object_id"]


class RestaurantCheckInResource(GenericCreateMixin, ModelResource):
    """
    Check-in AND Remove Check-In RESTAURANT
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
    model = CheckIn
    generic_model = Restaurant

    class Meta:
        queryset = CheckIn.objects.all()
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        resource_name = 'food-land-check-in'
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(),
                                             ApiKeyAuthentication())
        validation = FormValidation(form_class=CheckInForm)
        always_return_data = True
        include_resource_uri = False
        fields = ["id", "object_id"]


class RestaurantFavouriteResource(GenericCreateMixin, ModelResource):
    """
    Favourite AND Remove Favourite RESTAURANT
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
    generic_model = Restaurant

    class Meta:
        queryset = Favourite.objects.all()
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        resource_name = 'food-land-favourite'
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(),
                                             ApiKeyAuthentication())
        validation = FormValidation(form_class=FavouriteForm)
        always_return_data = True
        include_resource_uri = False
        fields = ["id", "object_id"]


class RestaurantRecommendResource(GenericCreateMixin, ModelResource):
    """
    Recommend AND Remove Recommend RESTAURANT
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
    generic_model = Restaurant

    class Meta:
        queryset = Recommend.objects.all()
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        resource_name = 'food-land-recommend'
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(),
                                             ApiKeyAuthentication())
        validation = FormValidation(form_class=RecommendForm)
        always_return_data = True
        include_resource_uri = False
        fields = ["id", "object_id"]


class RestaurantReviewResource(ModelResource):
    """
    Favourite AND Remove Favourite RESTAURANT
    @input params;
    {
    "object_id":36,
    "ApiKey tom:5b645a91095ee7b4837c10f5eaf86806e9f56c08"
    }
    @output params;
    {
    "id": 15,
    "object_id": 36,
    }
    """
    model = Review
    generic_model = Restaurant

    class Meta:
        queryset = Review.objects.all()
        allowed_methods = ['get', 'post']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        resource_name = 'food-land-review'
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(),
                                             ApiKeyAuthentication())
        validation = FormValidation(form_class=ReviewForm)
        always_return_data = True
        include_resource_uri = False
        fields = ["id", "object_id"]

    def obj_create(self, bundle, **kwargs):
        bundle.obj = self._meta.object_class()
        kwargs["user"] = bundle.request.user
        kwargs["content_type"] = ContentType.objects.get_for_model(self.generic_model)
        data = ast.literal_eval(bundle.request.body)
        review_text = data.get('review_text')
        object_id = data.get('object_id')
        instance = self.get_review_instance(object_id, bundle.request.user)
        if not review_text and instance:
            kwargs["id"], kwargs["pk"] = instance.id, instance.id
        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)
        bundle = self.full_hydrate(bundle)
        if not review_text and instance:
            self.update_food_land_rating(instance, data)
            return bundle
        return self.save(bundle)

    def get_review_instance(self, object_id, user):
        content_type = ContentType.objects.get_for_model(Restaurant)
        try:
            content_object = Review.objects.get(content_type=content_type, user=user,
                                                object_id=object_id, expire=False)
            return content_object
        except self.model.DoesNotExist:
            return None

    def update_food_land_rating(self, instance, data):
        instance.food_rating = data.get('food_rating') if data.get('food_rating') \
            else instance.food_rating
        instance.ambiance_rating = data.get('ambiance_rating') if data.get('ambiance_rating') \
            else instance.ambiance_rating
        instance.service_rating = data.get('service_rating') if data.get('service_rating') \
            else instance.service_rating
        instance.save()
        return True
