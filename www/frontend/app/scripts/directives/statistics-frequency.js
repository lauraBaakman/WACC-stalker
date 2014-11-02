define(['./module'], function(directives) {
    'use strict';
    directives.directive('statisticsFrequency', ['apiService',
        function(apiService, $scope) {
            return {
                restrict: 'E',
                scope: {
                    searchParameter: '=',
                    optionalSearchParameter: '='
                },
                templateUrl: '../views/statistics-frequency.html',
                controller: function(apiService, $scope) {
                    $scope.legend = {};

                    this.getData = function() {
                        $scope.data = {};
                        $scope.error = "";
                        apiService.getFrequency($scope.searchParameter, $scope.optionalSearchParameter).then(
                            function(result) {
                                $scope.data = {
                                    Data: {
                                        _type: "terms",
                                        terms: result.data
                                    }
                                };
                            },
                            function(error) {
                                $scope.error = error.data.message;
                            }
                        );
                    };

                    $scope.updateLegend = function(termObject, color, sum){
                        $scope.legend.term = termObject.term;
                        $scope.legend.color = color;
                        $scope.legend.percentage = ((termObject.count/sum) * 100).toFixed(2);
                };

                    this.getData();
                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
