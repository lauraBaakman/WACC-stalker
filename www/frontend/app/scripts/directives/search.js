define(['./module'], function (directives) {
    'use strict';
    directives.directive('search', [function ($scope) {
    	return {
    		restrict: 'E',
    		templateUrl: '../views/search.html',
    		controller: function() {
    			this.message = "Beste";

    			this.sayMessage = function() {
    				return this.message;
    			};
    		},
    		controllerAs: 'searchCtrl'
    	};
    }]);
});