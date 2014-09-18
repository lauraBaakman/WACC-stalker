define(['directives/directives'], function(directives) {
	directives.directive('search', ['$rootScope', function($rootScope) {
		return {
			restrict: 'E',
			templateUrl: '../../views/search.html',
			controller: function() {

			}
		};
	}]);
});