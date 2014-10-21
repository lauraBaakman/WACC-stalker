/**
 * Defines the main routes in the application.
 * The routes you see here will be anchors '#/' unless specifically configured otherwise.
 */

define(['./app'], function(app) {
    'use strict';
    return app.config(['$routeProvider', '$locationProvider',
        function($routeProvider, $locationProvider) {
            // Default goto the search page
            //$routeProvider.when('/', {
            //    redirectTo: '/search'
            //});

            // NOTE: Partial view for the search and search results
            $routeProvider.when('/', {
                templateUrl: 'views/search.html',
                //controller: 'MyCtrl1'
            });

            // NOTE: Partial view for the data (search) statistics
            $routeProvider.when('/statistics', {
                templateUrl: 'views/statistics.html',
                //controller: 'MyCtrl2'
            });

            // TODO: Build partial 404.html page
            $routeProvider.otherwise({
                templateUrl: 'views/404.html'
            });

            // Use the HTML5 History API: To remove the # in the url's
            //$locationProvider.html5Mode(true);
        }
    ]);
});
