define(['./module'], function(directives) {
    'use strict';
    directives.directive('statisticsFrequency', ['searchService',
        function(searchService, $scope) {
            return {
                restrict: 'E',
                scope: {
                    ratingValue: '='
                },
                templateUrl: '../views/statistics-frequency.html',
                controller: function($scope) {
                    console.log('Rating value in de controller:' + $scope.ratingValue);
                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
