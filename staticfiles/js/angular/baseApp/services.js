/**
 * Created by savad on 7/4/16.
 */

// Food lands listing
baseApp.factory("ListFoodsLands", [
    "$resource", "djangoUrl",
    function ($resource, djangoUrl) {
        return $resource(djangoUrl.reverse('api_dispatch_list', kwargs={'resource_name': 'food-lands-list', 'api_name': 'v1'}));
    }]);

// Dish listing
baseApp.factory("DishList", [
    "$resource", "djangoUrl",
    function ($resource, djangoUrl) {
        return $resource(djangoUrl.reverse('api_dispatch_list', kwargs={'resource_name': 'dish-detail', 'api_name': 'v1'}));
    }]);