define(['./module'], function(services){
	'use strict';

	services.service('apiService', ['$http', 
		function($http) {
			return {
				baseurl: 'http://127.0.0.1:5000/',
				
				getAllSearches: function() {
					console.log('getAllSearches in service is called.');
					return $http.get(this.baseurl + 'search').
						then(function(result){
							return result.data;
						});
				}
			};
		}
	]);
});