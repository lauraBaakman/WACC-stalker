define(['./module'], function(directives) {
    'use strict';
    directives.directive('facebook', [

        function($scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/facebook-results.html',
                controller: function($scope) {
                    // NOTE: Dummy results object
                    this.resultsAPI = {
                        "data": [{
                            "name": "Rick Van der Veen",
                            "id": "629307900522293"
                        }, {
                            "name": "Rick van der Veen",
                            "id": "337260969775811"
                        }, {
                            "name": "Rick Van der Veen",
                            "id": "629307900522293"
                        }, {
                            "name": "Rick Van der Veen",
                            "id": "629307900522293"
                        }, {
                            "name": "Rick Van der Veen",
                            "id": "629307900522293"
                        }]
                    };

                    $scope.results = this.resultsAPI.data;

                    this.search = function(id) {
                    	
                    };
                },
                controllerAs: 'facebookCtrl'
            };
        }
    ]);
});
