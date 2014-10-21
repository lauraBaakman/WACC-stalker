define(['./module'], function(directives) {
    'use strict';
    directives.directive('statisticsFrequency', ['apiService',
        function(apiService, $scope) {
            return {
                restrict: 'E',
                scope: {
                    searchParameter: '='
                },
                templateUrl: '../views/statistics-frequency.html',
                controller: function(apiService, $scope) {

                    this.getData = function() {
                        $scope.data = {};
                        $scope.error = {};
                        apiService.getFrequency($scope.searchParameter).then(
                            function(result) {
                                $scope.data = {
                                    Data: {
                                        _type: "terms",
                                        terms: result.data
                                    }
                                };
                                console.log($scope.data);
                            },
                            function(error) {
                                // TODO: Report to user
                                console.log('Error!');
                                $scope.error = 'The request for statistics has failed.';
                            }
                        );
                    };

                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
