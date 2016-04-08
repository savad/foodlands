/**
 * Created by savad on 7/4/16.
 */
/* Foodlands Page Controller */
FoodLandsApp.controller("FoodLandsController", [
    "$scope", 'djangoUrl', '$http', '$log', "ListFoodsLands",
    function ($scope, djangoUrl, $http, $log, ListFoodsLands) {

        // List food lands
        $scope.FoodLands = function ($event) {
            elmt = event.target;
            if('next_url_params' in $scope){
                next_url_params = $scope.next_url_params
            } else{
                var next_url_params = {};
                $scope.food_lands = []
            }
            var fetchItemURL = djangoUrl.reverse('foodlands');
            console.log(fetchItemURL)
            ListFoodsLands.get(next_url_params, function (data) {
                console.log(data.objects)
                $scope.food_lands = $scope.food_lands.concat(data.objects);
                if(data.next) {
                    $scope.next_url_params = getUrlVars(data.next);
                } else{
                    $scope.more_food_lands = true;
                }
            })
        };


    }
]);





