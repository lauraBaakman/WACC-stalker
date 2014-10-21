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

                    $scope.test = function(term, color){
                        console.log(term);
                    };



                    this.getData();
                },
                controllerAs: 'freqStatCtrl'
            };
        }
    ]);
});
