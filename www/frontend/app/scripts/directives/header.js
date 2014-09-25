define(['./module'], function(directives) {
    'use strict';
    directives.directive('header', [

        function($scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/header.html',
                controller: function($scope) {
                    // This shouldn't be a controller but couldnt't get it work with ng-include.
                },
            };
        }
    ]);
});
