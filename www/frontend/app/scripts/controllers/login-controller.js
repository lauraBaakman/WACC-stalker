define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('LoginCtrl', ['$scope', 'stalkerService',

        function($scope, stalkerService) {
            $scope.error = "";
            var controller = this;      

            /* Supported social media and other directives. */
            var directives = [
                {
                    loggedIn: false,
                    loginView: '../views/facebook/facebook.html',
                    logo: 'facebook'

                },
                {
                    loggedIn: false,
                    loginView: '../views/linkedin/linkedin.html',
                    logo: 'linkedin'
                }
            ];

            this.startStalking = function(){
                stalkerService.commitStalker();
                if(stalkerService.isLoggedIn()){
                    $scope.stalking = true;
                } else {
                    $scope.error = " You need to be logged on to at least one social network.";
                }
            };

            $scope.$on('loggedInEvent', function (event, data) {
                $scope.error = "";
                directives.social[data].loggedIn = true;
            });

            $scope.$on('loggedOutEvent', function (event, data) {
                $scope.error = " You need to be logged on to at least one social network.";
                directives.social[data].loggedIn = false;
            });            

        }
    ]);
});
