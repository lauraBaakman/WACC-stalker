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

                getFrequency : function(param, optionalParam) {
                    if(optionalParam){
                        return $http.get(this.baseurl + 'statistics/' + param + '/frequency/' + optionalParam);    
                    } else {
                        return $http.get(this.baseurl + 'statistics/' + param + '/frequency');    
                    }
                },

                // POSTS
                postSearch: function(postData) {
					return $http.post(this.baseurl + 'searches', postData);
                },

                postStalker: function(postData) {
                	return $http.post(this.baseurl + 'stalkers', postData);
                },  

                postVictim: function(postData) {
					return $http.post(this.baseurl + 'victims', postData);
                }             
            };
        }
    ]);
});
