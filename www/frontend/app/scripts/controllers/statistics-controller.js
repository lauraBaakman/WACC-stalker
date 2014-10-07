define(['./module'], function(controllers) {
	'use strict';
	controllers.controller('StatisticsController', ['$scope', 'apiService',

		function($scope, apiService){
			$scope.searches = [];
			$scope.error = {};

			this.getAllSearches = function() {
				$scope.searches = [];
				$scope.error = {};
				apiService.getAllSearches().then(
					function(searches){
						$scope.searches = searches;
					},
					function(error){
						$scope.error = 'The request for all searches failed.';
					}
				);
			};
		}
	]);
});