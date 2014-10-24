define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('LoginCtrl', ['$scope', 'stalkerService',

        function($scope, stalkerService) {
            $scope.error = "";
            $scope.stalking = false;
            var controller = this;

            $scope.carousel = {
                activePage: 0,
                move: function(direction) {
                    return ($scope.carousel.activePage + direction + numSocialMedia) % numSocialMedia;
                },
                isActive: function(page) {
                    return page == $scope.carousel.activePage;
                }
            };

            $scope.socialMedia = {
                media: {
                    facebook: {
                        loggedIn: false,
                        loginView: '../views/facebook/facebook.html',
                        logo: 'facebook'
                    },
                    linkedIn: {
                        loggedIn: false,
                        loginView: '../views/linkedin/linkedin.html',
                        logo: 'linkedin'
                    }             
                },

                showWell: function(pageNumber, name) {
                    return ( 
                        ($scope.stalking && $scope.socialMedia.media[name].loggedIn) ||
                        (!$scope.stalking && $scope.carousel.isActive(pageNumber)));
                }
            };


            this.startStalking = function() {
                if (stalkerService.isLoggedIn()) {
                    stalkerService.commitStalker();
                    $scope.stalking = true;
                    $scope.error = "";
                } else {
                    $scope.error = " You need to be logged on to at least one social network.";
                }
            };

            // Keep the socialMedia array up to data, 
            // TODO: Fix so that it works with the new array
            $scope.$on('loggedInEvent', function(event, data) {
                $scope.socialMedia.media[data].loggedIn = true;
            });

            $scope.$on('loggedOutEvent', function(event, data) {
                $scope.socialMedia.media[data].loggedIn = false;
            });

            var numSocialMedia = Object.keys($scope.socialMedia.media).length;
        }
    ]);
});
