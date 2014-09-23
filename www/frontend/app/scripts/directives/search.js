define(['./module'], function(directives) {
    'use strict';
    directives.directive('search', [

        function($scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/search-field.html',
                controller: function($scope) {
                    // Initialization: They need to be empty strings ("") so we can use
                    // String.isEmpty(), which is a non-native function and defined 
                    // in scripts/bootstrap.js
                    this.init = function() {
                        this.search = {
                            name: "",
                            email: ""
                        };

                        // Error message
                        this.error = "";
                    }

                    // Check if all the fields are empty
                    this.isSearchEmpty = function() {
                        return (this.search.name.isEmpty() && this.search.email.isEmpty());
                    };

                    // Align the submit button to the input fields
                    $('.pull-down').each(function() {
                        $(this).css('margin-top', $(this).prev().height() - $(this).height());
                    });

                    // Apply bootstrap classes based on angular error classes
                    $("input").change(function(event) {
                        // Avoid validating empty inputs
                        if (!$(this).val().length) {
                            $(this).parent().removeClass('has-error').removeClass('has-success');
                        } else if ($(this).hasClass('ng-invalid')) {
                            $(this).parent().addClass('has-error');
                        } else if ($(this).hasClass('ng-valid')) {
                            $(this).parent().addClass('has-success');
                        }
                    });

                    // Remove error class on focus
                    $("input").focus(function(event) {
                        $(this).parent().removeClass('has-error');
                    });

                    this.resetForm = function() {
                        // $scope.searchForm.$setPristine();
                        // Reset on the model
                        this.init();

                        // Reset on the css
                        $('form').children('.form-group')
                            .removeClass('has-success')
                            .removeClass('has-error');
                    };

                    this.searchSubmit = function(noCheck) {
                        noCheck = typeof noCheck !== 'undefined' ? noCheck : false;
                        if (noCheck) { // Submit without validation
                            console.log('Submitting!');
                            this.resetForm();
                        } else { // Submit with validation
                            if(this.isSearchEmpty()) {
                                this.error = " We need at least a name or an email address in order to search.";
                                console.log('no name and no email');
                            } else if (this.search.name.isEmpty()) {
                                this.error = " We need a name for some social networks.";
                                console.log('no name');
                            } else if (this.search.email.isEmpty()) {
                                this.error = " We need an email address for some social networks.";
                                console.log('no email');
                            } else {
                                console.log('Submitting!');
                                this.resetForm();
                            }
                        }
                    };
                },
                controllerAs: 'searchCtrl'
            };
        }
    ]);
});
