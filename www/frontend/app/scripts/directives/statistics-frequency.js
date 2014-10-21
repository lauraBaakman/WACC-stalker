define(['./module'], function(directives) {
    'use strict';
    directives.directive('statisticsFrequency', ['searchService',
        function(searchService, $scope) {
            return {
                restrict: 'E',
                scope: {
                    searchParameter: '='
                },
                templateUrl: '../views/statistics-frequency.html',
                controller: function($scope) {
                    console.log('Input in de controller:' + $scope.searchParameter);
                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
