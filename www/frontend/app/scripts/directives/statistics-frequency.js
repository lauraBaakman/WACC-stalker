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
                // link: function(scope, elem, attrs) {
                //     scope.stars = [];
                //     console.log(scope.ratingValue);
                //     for (var i = 0; i < scope.ratingValue; i++) {
                //         scope.stars.push({});
                //     }
                // },
                controller: function($scope) {
                    console.log('Rating value in de controller:' + $scope.ratingValue);
                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
