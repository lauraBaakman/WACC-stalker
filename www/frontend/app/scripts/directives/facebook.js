define(['./module'], function(directives) {
    'use strict';
    directives.directive('search', [

        function($scope) {
            return {
                restrict: 'E',
                templateUrl: '../views/search-field.html',
                controller: function($scope) {
                    // NOTE: Dummy results object
                    this.results = {
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

                    
                }
            };
        };
    ]);
});
