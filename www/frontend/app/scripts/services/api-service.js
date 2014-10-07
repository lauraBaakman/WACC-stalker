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
                    var request = $http({
                        method: 'post',
                        url: baseurl + 'search',
                        data: postData
                    });
                    return(request.then( handleSuccess, handleError));
                },

                postStalker: function(postData) {
                    var request = $http({
                        method: 'post',
                        url: baseurl + 'stalker',
                        data: postData
                    });
                    return(request.then( handleSuccess, handleError));
                },  

                postVictim: function(postData) {
                    var request = $http({
                        method: 'post',
                        url: baseurl + 'victim',
                        data: postData
                    });
                    return(request.then( handleSuccess, handleError));
                }             
            };
        }
    ]);
});
