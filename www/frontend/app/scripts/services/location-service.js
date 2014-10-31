define(['./module'], function(services) {
    'use strict';

    services.service('locationService', ['$http',
        function($http) {
            return {

                getLocationFromIP: function() {
                    var location = {
                        latitude: null,
                        longitude: null,
                        country_code: null
                    };

                    return $http.get('http://freegeoip.net/json/').then(
                        function(result) {
                            location.country_code = result.data.country_code;
                            location.latitude = result.data.latitude;
                            location.longitude = result.data.longitude;
                            return location;
                        },
                        function(error) {
                            console.log(error);
                            return location;
                        }
                    );
                }
            };
        }
    ]);
});
