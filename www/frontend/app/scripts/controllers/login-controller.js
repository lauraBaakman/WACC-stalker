define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('LoginCtrl', ['$scope', 'stalkerService',

        function($scope, stalkerService) {
            $scope.controllername = "LoginCtrl"
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
                if(stalkerService.isLoggedIn()){
                    console.log('stalkerService.isLoggedIn returned true');
                    $scope.stalking = true;
                    stalkerService.commitStalker();
                } else {
                    console.log('stalkerService.isLoggedIn returned false');
                    $scope.error = " You need to be logged on to at least one social network.";
                }
            };

            $scope.$on('loggedInEvent', function (event, data) {
                console.log(data);
                $scope.error = "";
                directives.social[data].loggedIn = true;
            });

            $scope.$on('loggedOutEvent', function (event, data) {
                console.log(data);
                $scope.error = " You need to be logged on to at least one social network.";
                directives.social[data].loggedIn = false;
            });            

        }
    ]);
});
