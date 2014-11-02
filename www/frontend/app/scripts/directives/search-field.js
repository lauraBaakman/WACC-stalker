define(['./module'], function(directives) {
    'use strict';
    directives.directive('searchField', ['apiService', 'stalkerService', 'locationService', 'searchService',
        function(apiService, stalkerService, locationService, searchService, $scope) {
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

                    $scope.warning = "";

                    // Check if all the fields are empty
                    this.isSearchEmpty = function() {
                        // Angular removes the field so then isEmpty won't work.
                        if ($scope.search.email == null) {
                            return ($scope.search.name.isEmpty());
                        }
                        return ($scope.search.name.isEmpty() && $scope.search.email.isEmpty());
                    };

                    // Apply bootstrap classes based on angular error classes
                    $("input").change(function(event) {
                        // Clear error
                        $scope.warning = "";

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
                        $scope.warning = "";

                        $(this).parent().removeClass('has-error');
                    });

                    this.resetForm = function() {
                        // $scope.searchForm.$setPristine();
                        $scope.search = angular.copy(search);
                        $scope.warning = "";

                        // Reset on all angularmagic
                        $scope.searchForm.$setPristine();

                        // Reset on the css
                        $('form').children('.form-group')
                            .removeClass('has-success')
                            .removeClass('has-error');
                    };

                    this.validate = function() {
                        if (this.isSearchEmpty()) {
                            $scope.warning = " We need at least a name or an email address in order to search.";
                        } else if ($scope.search.name.isEmpty()) {
                            $scope.warning = " We need a name for some social networks.";
                        } else if ($scope.search.email.isEmpty()) {
                            $scope.warning = " We need an email address for some social networks.";
                        } else {
                            this.resetForm();
                        }
                    };

                    this.searchSubmit = function(noCheck) {
                        noCheck = typeof noCheck !== 'undefined' ? noCheck : false;
                        if (noCheck) { // Submit without validation
                            var search = {};
                            locationService.getLocationFromIP().then(
                                function(result) {
                                    search = result;
                                    search.stalker_id = stalkerService.getStalkerId();
                                    apiService.postSearch(search).then(
                                        function(result){
                                            stalkerService.setMostRecentSearch(result.data.data);
                                        },
                                        function(error){
                                            stalkerService.setMostRecentSearch(null);
                                        }
                                    );
                                }
                            );
                            searchService.broadcast({
                                "name": $scope.search.name,
                                "email": $scope.search.email
                            });
                            this.resetForm();
                        } else { 
                            // Submit with validation
                            this.validate();
                        }
                    };
                },
                controllerAs: 'searchCtrl'
            };
        }
    ]);
});
