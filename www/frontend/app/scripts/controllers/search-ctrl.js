define(['./module'], function(controllers) {
    'use strict';
    controllers.controller('SearchCtrl', [
        function($scope) {
            // Controller controls the search, login carousel and when to show which 
            // social media directives

            var directives = {
                social: {
                    "facebook": {
                        enabled: false,
                        loginView: '../views/facebook/login-facebook.html',
                        logo: 'fa-facebook',

                    },
                    "linkedIn": {
                        enabled: false,
                        loginView: '../views/linkedin/login-linkedin.html',
                        logo: 'fa-linkedin',
                    }
                },
                "search": {
                    enabled: false
                }
            };

            this.isEnabled = function(medium) {
            	var directive = directives[medium];
                if(directive !== null) {
                	return directive.enabled;
                } 
                directive = directives.social[medium];
                if(directive !== null) {
                	return directive.enabled;
                }
                return false;
            };

            this.setEnabled = function(medium, bool) {
                var directive = directives[medium];
                if(directive !== null) {
                	directive.enabled = bool;
                	return true;
                }
                directive = directives.social[medium];
                if(directive !== null) {
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
