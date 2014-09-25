define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('SearchCtrl', ['$scope',

        function($scope) {
            // Controller controls the search, login carousel and when to show which 
            // social media directives
            this.currentPage = 0;
            this.numberOfSupportedSocialMedia = 2;

            this.isActive = function(pageNo) {
                return pageNo == this.currentPage;
            };

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

            var directives = {
                social: {
                    "facebook": {
                        enabled: false,
                        loginView: '../views/facebook/login-facebook.html',
                        logo: 'facebook'

                    },
                    "linkedIn": {
                        enabled: false,
                        loginView: '../views/linkedin/login-linkedin.html',
                        logo: 'linkedin'
                    }
                },
                "search": {
                    enabled: false
                }
            };

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
        }
    ]);
});
