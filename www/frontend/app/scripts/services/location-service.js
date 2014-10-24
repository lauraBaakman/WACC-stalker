define(['./module'], function(services) {
    'use strict';

    services.service('locationService', ['$http',
        function($http) {
            return {

                getLocationFromIp: function() {
                    var location = {
                        latitude: null,
                        longitude: null,
                        country_code: null
                    };

                    $http.get('http://freegeoip.net/json/').then(
                        function(result) {
                            console.log(result);
                            location.country_code = result.Data.country_code;
                            location.latitude = result.Data.latitude;
                            location.longitude = result.Data.longitude;
                        },
                        function(error) {
                            //Return the empty location
                        }
                    );
                    return location;
                }
            };
        }
    ]);
});
