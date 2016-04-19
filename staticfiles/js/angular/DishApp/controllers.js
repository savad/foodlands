/**
 * Created by savad on 7/4/16.
 */
/* Dish Listing Page Controller */
DishApp.controller("DishListController", [
    "$scope", 'djangoUrl', '$http', '$log', "DishList",
    function ($scope, djangoUrl, $http, $log, DishList) {

        // List food lands
        $scope.DishList = function ($event) {
            elmt = event.target;
            if('next_url_params' in $scope){
                next_url_params = $scope.next_url_params
            } else{
                var next_url_params = {};
                $scope.dish_list = []
            }
            DishList.get(next_url_params, function (data) {
                console.log(data.objects)
                $scope.dish_list = $scope.dish_list.concat(data.objects);
                if(data.next) {
                    $scope.next_url_params = getUrlVars(data.next);
                } else{
                    $scope.more_dishes = true;
                }
            })
        };
    }
]);