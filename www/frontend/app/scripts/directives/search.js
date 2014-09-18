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

                // Apply bootstrap classes based on angular error classes
                $("input").change(function(event) {
                    // Avoid validating empty inputs
                    if(!$(this).val().length){
                        $(this).parent().removeClass('has-error').removeClass('has-success');
                    }

                    // No need to check for ng-dirty since this is activated on change
                    if ($(this).hasClass('ng-invalid')) {
                        $(this).parent().addClass('has-error');
                    } else if ($(this).hasClass('ng-valid')) {
                        $(this).parent().addClass('has-success');
                    }
                });

                // Remove error class on focus
                $("input").focus(function(event) {
                    $(this).parent().removeClass('has-error');
                });

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