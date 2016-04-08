/**
 * Created by savad on 7/4/16.
 */


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Read a page's GET URL variables and return them as an associative array.
function getUrlVars(url)
{
    var regex = /[?&]([^=#]+)=([^&#]*)/g,
    params = {},
    match;
    while(match = regex.exec(url)) {
        params[match[1]] = match[2];
    }
    return params;
}

var baseApp = angular.module("baseApp", ["djng.urls", "ngResource"]);

// Don't strip trailing slashes from calculated URLs
baseApp.config(['$resourceProvider', function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

// HTTP requests need to be considered AJAX requests.
baseApp.config(["$httpProvider", function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";
    $httpProvider.defaults.headers.post['X-CSRFToken'] = getCookie('csrftoken');
}]);
