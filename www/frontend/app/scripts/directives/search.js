define(['./module'], function (directives) {
    'use strict';
    directives.directive('search', [function ($scope) {
    	return {
    		restrict: 'E',
    		templateUrl: '../views/search.html',
    		controller: function() {
    			this.search = {};

    			this.sayMessage = function() {
    				return this.message;
    			};

                this.searchSubmit = function(){
                    alert("Submitting the form!");

                    // reset the this.search after submit to clear the form
                    this.search = {};
                };
    		},
    		controllerAs: 'searchCtrl'
    	};
    }]);
});