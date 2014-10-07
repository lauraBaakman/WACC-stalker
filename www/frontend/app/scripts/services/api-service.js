define(['./module'], function(services) {
    'use strict';

    services.service('apiService', ['$http',
        function($http) {
            return {
                baseurl: 'http://127.0.0.1:5000/',

                // GETS
                getAllSearches: function() {
                    return $http.get(this.baseurl + 'search').
                    then(function(result) {
                        return result.data;
                    });
                },

                getAllStalkers: function() {
                    return $http.get(this.baseurl + 'stalker').
                    then(function(result) {
                        return result.data;
                    });
                },

                getAllVictims: function() {
                    return $http.get(this.baseurl + 'victim').
                    then(function(result) {
                        return result.data;
                    });
                },

                // POSTS
                postSearch: function(postData) {
					return $http.post(this.baseurl + 'search', postData);
                },

                postStalker: function(postData) {
                	return $http.post(this.baseurl + 'stalker', postData);
                },  

                postVictim: function(postData) {
					return $http.post(this.baseurl + 'victim', postData);
                }             
            };
        }
    ]);
});
