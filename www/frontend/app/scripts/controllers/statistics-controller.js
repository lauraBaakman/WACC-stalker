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
						console.log('Error!')
						$scope.error = 'The request for all searches failed.';
					}
				);
			};

			this.getAllStalkers = function() {
				$scope.stalkers = [];
				$scope.error = {};
				apiService.getAllStalkers().then(
					function(stalkers){
						$scope.stalkers = stalkers;
					},
					function(error){
						console.log('Error!')
						$scope.error = 'The request for all stalkers failed.';
					}
				);
			};

			this.getAllVictims = function() {
				$scope.victims = [];
				$scope.error = {};
				apiService.getAllVictims().then(
					function(victims){
						$scope.victims = victims;
					},
					function(error){
						console.log('Error!')
						$scope.error = 'The requenst for all victims failed.';
					}
				);
			};			
		}
	]);
});