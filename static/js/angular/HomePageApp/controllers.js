/* home Page Controller */
HomePageApp.controller("HomePageController", [
    "$scope", "UserFollow", "UserUnFollow", "VideoLikeApp", "RemoveVideoLikeApp",
    function ($scope, UserFollow, UserUnFollow, VideoLikeApp, RemoveVideoLikeApp) {

        // follow user from home page
        $scope.FollowFromHomePage = function ($event, user_id) {
            elmt = event.target;
            if (elmt.className=="following-btn"){
                UserUnFollow.remove({"pk": elmt.getAttribute('dataId')}, function (data) {
                    $(elmt).attr('class', 'follow-btn')
                    $(elmt).html("Follow")
                })
            }
            else if (elmt.className=="follow-btn"){
                UserFollow.save({"following": user_id}, function (data) {
                    $(elmt).attr('class', 'following-btn')
                    elmt.setAttribute("dataId", data.id);
                    $(elmt).html("Following")
                })
            }
        return false;
        };

        // video like/Unlike in home page
        $scope.HomePageVideoLike = function ($event, video_id) {
            elmt = event.target;
            className = elmt.parentNode.parentNode.className
            id="video-like-count-"+video_id;
            var video_count = document.getElementById(id).innerHTML;
            video_count = parseInt(video_count);
            elmt.parentNode.parentNode.className == "TS-vd-like-temp"
            if (className == "TS-vd-like") {
                VideoLikeApp.save({"object_id": video_id}, function (data) {
                    elmt.setAttribute('dataId', data.id);
                    video_count=video_count+1;
                    document.getElementById(id).innerHTML=video_count;
                    elmt.parentNode.parentNode.className = "TS-vd-liked";
                });
            }
            else if (className == "TS-vd-liked") {
                RemoveVideoLikeApp.remove({"pk": elmt.getAttribute('dataId')}, function (data) {
                    video_count=video_count-1;
                    document.getElementById(id).innerHTML=video_count;
                    elmt.parentNode.parentNode.className = "TS-vd-like";
                    });
            }
        };
    }
]);



