define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('LoginCtrl', ['$scope', 'stalkerService',

        function($scope, stalkerService) {
            $scope.error = "";
            var controller = this;

            $scope.carousel = {
                activePage: 0,
                move: function(direction) {
                    return ($scope.carousel.activePage + direction + controller.socialMedia.length) % controller.socialMedia.length;
                }
            };

            /* Supported social media and other socialMedia. */
            this.socialMedia = [{
                loggedIn: false,
                loginView: '../views/facebook/facebook.html',
                logo: 'facebook'

            }, {
                loggedIn: false,
                loginView: '../views/linkedin/linkedin.html',
                logo: 'linkedin'
            }];

            this.startStalking = function() {
                if (stalkerService.isLoggedIn()) {
                    console.log('stalkerService.isLoggedIn returned true');
                    $scope.stalking = true;
                    stalkerService.commitStalker();
                } else {
                    console.log('stalkerService.isLoggedIn returned false');
                    $scope.error = " You need to be logged on to at least one social network.";
                }
            };

            // Keep the socialMedia array up to data, 
            // TODO: Fix so that it works with the new array
            $scope.$on('loggedInEvent', function(event, data) {
                console.log(data);
                $scope.error = "";
                socialMedia.social[data].loggedIn = true;
            });

            $scope.$on('loggedOutEvent', function(event, data) {
                console.log(data);
                $scope.error = " You need to be logged on to at least one social network.";
                socialMedia.social[data].loggedIn = false;
            });

        }
    ]);
});
