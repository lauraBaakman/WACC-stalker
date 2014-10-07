define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('SearchCtrl', ['$scope', 'stalkerService',

        function($scope, stalkerService) {
            // Controller controls the search, login carousel and when to show which 
            // social media directives
            this.currentPage = 0;
            this.numberOfSupportedSocialMedia = 2;
            $scope.error = "";
            $scope.stalking = false;
            var controller = this;

            /* Caroussel functions */
            this.isActive = function(pageNo) {
                return pageNo == this.currentPage;
            };

            this.showInResults = function(pageNo, medium){
                if($scope.stalking){
                    return medium.loggedIn;
                }
                return this.isActive(pageNo);
            }

            this.setPage = function(index) {
                this.currentPage = index;
            };

            this.back = function(){
                this.setPage(
                    (this.currentPage - 1 + this.numberOfSupportedSocialMedia) % 
                    this.numberOfSupportedSocialMedia);
            };  

            this.forward = function(){
                this.setPage(
                    (this.currentPage + 1 + this.numberOfSupportedSocialMedia) % 
                    this.numberOfSupportedSocialMedia);
            };         

            /* Supported social media and other directives. */
            var directives = {
                social: {
                    "facebook": {
                        loggedIn: false,
                        loginView: '../views/facebook/facebook.html',
                        logo: 'facebook'

                    },
                    "linkedIn": {
                        loggedIn: false,
                        loginView: '../views/linkedin/linkedin.html',
                        logo: 'linkedin'
                    }
                },
                "search": {
                    enabled: false
                }
            };

            /* Edit and request the data in directives. */
            this.isEnabled = function(medium) {
                var directive = directives[medium];
                if (directive !== null) {
                    return directive.enabled;
                }
                directive = directives.social[medium];
                if (directive !== null) {
                    return directive.enabled;
                }
                return false;
            };

            this.setEnabled = function(medium, bool) {
                var directive = directives[medium];
                if (directive !== null) {
                    directive.enabled = bool;
                    return true;
                }
                directive = directives.social[medium];
                if (directive !== null) {
                    directive.enabled = bool;
                    return true;
                }
                return false;
            };

            this.getSocialMedia = function() {
                return directives.social;
            };

            this.getDirectives = function(){
                return directives;
            }

            this.startStalking = function(){
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
