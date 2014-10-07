define(['./module'], function(controllers) {
	'use strict';
	controllers.controller('StatisticsController', ['$scope', 'apiService',

		function($scope, apiService){
			$scope.searches = '';

			this.getAllSearches = function() {
				console.log('getAllSearches in controller is called.');
				apiService.getAllSearches().then(
					function(searches){
						console.log('getAllSearches has success.');
						console.log(searches);
					},
					function(error){
						console.log('getAllSearches has error.');
						console.log(error);
					}
				);
			};

			this.test = function(){
				console.log(apiService.test());
				return apiService.test();
			};
		}
	]);
});