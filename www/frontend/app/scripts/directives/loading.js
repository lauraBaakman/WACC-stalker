// adapted from: http://stackoverflow.com/questions/17144180/angularjs-loading-screen-on-ajax-request

define(['./module'], function(directives) {
    'use strict';
    directives.directive('loading', ['$http',

        function($http) {
            return {
                restrict: 'A',
                link: function(scope, elm, attrs) {
                    scope.isLoading = function() {
                        return $http.pendingRequests.length > 0;
                    };

                    scope.$watch(scope.isLoading, function(v) {
                        if (v) {
                            elm.show();
                        } else {
                            elm.hide();
                        }
                    });
                }
            };
        }
    ]);
});
