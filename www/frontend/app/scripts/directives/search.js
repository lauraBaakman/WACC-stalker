define(['./module'], function (directives) {
    'use strict';
    directives.directive('search', [function ($scope) {
    	return {
    		restrict: 'E',
    		templateUrl: '../views/search.html',
    		controller: function() {
    			this.search = {};

                // Align the submit button to the input fields
                $('.pull-down').each(function() {
                    $(this).css('margin-top', $(this).prev().height()-$(this).height());
                });

                $("input").change(function(event) {
                    console.log($(this));
                    if ($(this).hasClass('ng-dirty ng-invalid')) {
                        $(this).parent().addClass('debug');
                    }
                });

                $("input").focus(function(event) {
                    $(this).parent().removeClass('debug');
                });
                    


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