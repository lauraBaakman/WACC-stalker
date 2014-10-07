define(['./module'], function(services){
	'use strict';

	services.service('apiService', ['$http', 
		function($http) {
			return {
				//todo url eruit trekken naar base url
				getAllSearches: function() {
					console.log('getAllSearches in service is called.');
					return $http.get('http://127.0.0.1:5000/search').
						then(function(result){
							return result.data;
						});
				}
			};
		}
	]);
});