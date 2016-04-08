/**
 * Created by savad on 7/4/16.
 */
baseApp.factory("ListFoodsLands", [
    "$resource", "djangoUrl",
    function ($resource, djangoUrl) {
        return $resource(djangoUrl.reverse('api_dispatch_list', kwargs={'resource_name': 'food-lands-list', 'api_name': 'v1'}));
    }]);
