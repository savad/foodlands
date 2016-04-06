__author__ = 'savad'
from tastypie.api import Api

from applications.api.foodlands import api as food_lands_api
from applications.api.foodland_specifications import api as food_lands_specifications_api
from applications.api.locations import api as locations_api
from applications.api.dishes import api as dishes_api


v1_api = Api(api_name='v1')
v1_api.register(food_lands_api.BaseRestaurantResource())
v1_api.register(food_lands_api.RestaurantResource())
v1_api.register(food_lands_specifications_api.CourseResource())
v1_api.register(food_lands_specifications_api.CuisineResource())
v1_api.register(food_lands_specifications_api.ServeResource())
v1_api.register(food_lands_specifications_api.SuitableResource())
v1_api.register(food_lands_specifications_api.HighLightResource())
v1_api.register(locations_api.CountryResource())
v1_api.register(locations_api.StateResource())
v1_api.register(locations_api.CityResource())
v1_api.register(locations_api.PlaceResource())
v1_api.register(dishes_api.BaseDishResource())
v1_api.register(dishes_api.DishResource())
