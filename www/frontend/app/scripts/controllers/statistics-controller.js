define(['./module'], function(controllers) {
	'use strict';
	controllers.controller('StatisticsController', ['$scope', 'apiService',

		function($scope, apiService){
			$scope.searches = [];

			this.getAllSearches = function() {
				apiService.getAllSearches().then(
					function(searches){
						console.log('getAllSearches had success');
						$scope.searches = searches;
					},
					function(error){
						console.log('getAllSearches had an error');
						$scope.error = 'The request for all searches failed.';
					}
				);
			};
		}
	]);
});