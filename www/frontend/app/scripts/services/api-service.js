define(['./module'], function(services){
	'use strict';

	services.service('apiService', ['$http', 
		function($http) {
			return {
				baseurl: 'http://127.0.0.1:5000/',
				
				getAllSearches: function() {
					return $http.get(this.baseurl + 'search').
						then(function(result){
							return result.data;
						});
				},

				getAllStalkers: function() {
					console.log('in get all stalkers in de service')
					return $http.get(this.baseurl + 'stalker').
						then(function(result){
							return result.data;
						});					
				},

				getAllVictims: function() {
					return $http.get(this.baseurl + 'victim').
						then(function(result){
							return result.data;
						});					
				}				
			};
		}
	]);
});