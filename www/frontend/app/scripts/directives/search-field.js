define(['./module'], function(directives) {
    'use strict';
    directives.directive('searchField', ['searchService',
        function(searchService, $scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/search-field.html',
                controller: function(searchService, $scope) {
                    // Initialization: They need to be empty strings ("") so we can use
                    // String.isEmpty(), which is a non-native function and defined 
                    // in scripts/bootstrap.js
                    var search = {
                        name: "",
                        email: ""
                    };

                    $scope.search = angular.copy(search);

                    $scope.error = "";

                    // Check if all the fields are empty
                    this.isSearchEmpty = function() {
                        // Angular removes the field so then isEmpty won't work.
                        if ($scope.search.email === null) {
                            return ($scope.search.name.isEmpty());
                        }
                        return ($scope.search.name.isEmpty() && $scope.search.email.isEmpty());
                    };

                    // Align the submit button to the input fields
                    $('.pull-down').each(function() {
                        $(this).css('margin-top', $(this).prev().height() - $(this).height());
                    });

                    // Apply bootstrap classes based on angular error classes
                    $("input").change(function(event) {
                        // Clear error
                        $scope.error = "";

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
                        // Clear error
                        $scope.error = "";

                        $(this).parent().removeClass('has-error');
                    });

                    this.resetForm = function() {
                        // $scope.searchForm.$setPristine();
                        $scope.search = angular.copy(search);
                        $scope.error = "";

                        // Reset on all angularmagic
                        $scope.searchForm.$setPristine();

                        // Reset on the css
                        $('form').children('.form-group')
                            .removeClass('has-success')
                            .removeClass('has-error');
                    };

                    this.validate = function() {
                        if (this.isSearchEmpty()) {
                            $scope.error = " We need at least a name or an email address in order to search.";
                            console.log('no name and no email');
                        } else if ($scope.search.name.isEmpty()) {
                            $scope.error = " We need a name for some social networks.";
                            console.log('no name');
                        } else if ($scope.search.email.isEmpty()) {
                            $scope.error = " We need an email address for some social networks.";
                            console.log('no email');
                        } else {
                            console.log('Submitting!');
                            this.resetForm();
                        }
                    };

                    this.searchSubmit = function(noCheck) {
                        noCheck = typeof noCheck !== 'undefined' ? noCheck : false;
                        if (noCheck) { // Submit without validation
                            console.log('Submitting!');
                            console.log(searchService);
                            searchService.broadcast({"name": $scope.search.name, "email": $scope.search.email});
                            this.resetForm();
                        } else { // Submit with validation
                            this.validate();
                        }
                    };
                },
                controllerAs: 'searchCtrl'
            };
        }
    ]);
});
