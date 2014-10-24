define(['./module'], function(services) {
    'use strict';

    services.service('apiService', ['$http',
        function($http) {
            return {
                getLocationFromIp : function() {

                },

                fromCountryCodeToName : function() {

                },

                fromCountryNameToCode : function() {

                }
            };
        }
    ]);
});
