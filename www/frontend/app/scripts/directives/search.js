define(['./module'], function(directives) {
    'use strict';
    directives.directive('search', [
        function($scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/search.html',
                controller: function($scope) {
                    this.search = {};

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
                        this.search = {};
                        $("form").children('.form-group').
                        removeClass('has-success').
                        removeClass('has-error');
                    };

                    this.searchSubmit = function(noCheck) {
                        noCheck = typeof noCheck !== 'undefined' ? noCheck : false;
                        if (noCheck) {
                            console.log('Submitting!');
                            this.resetForm();
                        } else {

                            if (!this.search.name) {
                                this.error = "We need a name for some social networks";
                                console.log('no name');
                            } else if (!this.search.email) {
                                this.error = "We need an email address for some social networks.";
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
