define(['./module'], function(directives) {
    'use strict';
    directives.directive('statisticsFrequency', ['searchService',
        function(searchService, $scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/statistics-frequency.html',
                controller: function($scope) {
                    console.log('stat-freq-controller');
                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
