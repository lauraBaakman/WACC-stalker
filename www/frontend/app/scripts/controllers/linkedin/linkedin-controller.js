define(['../module'], function(controllers, ngLinkedin) {
    'use strict';
    controllers.controller('LinkedInController', ['$scope', '$linkedIn', 'searchService', 'stalkerService',
        function($scope, $linkedIn, searchService, stalkerService) {

            var controller = this;

            // Initialization data objects
            $scope.search = null;
            $scope.results = null;
            $scope.person = null;
            $scope.user = null;

            // Initialization navigation
            $scope.pages = {
                login: 1,
                results: 2,
                detail: 3
            };

            /* ------------------ Data manipulation ------------------ */

            this.hasResults = function() {
                return ($scope.results !== null);
            };

            this.hasDetail = function() {
                return ($scope.person !== null);
            };

            this.clearResults = function() {
                $scope.results = null;
            };

            this.clearPerson = function() {
                $scope.person = null;
            };

            /* ------------------ LinkedIn API calls ------------------ */

            this.login = function() {
                $linkedIn.authorize().then(function() {
                    if ($linkedIn.isAuthorized()) {
                        console.log("LINKEDINCONTROLLER: Logged in and authorized");
                        controller.setPage($scope.pages.results);
                        //$linkedIn.peopleSearch({'first-name': 'Rick', 'last-name': 'van Veen'}).then(function(result) {
                        //	console.log(result);
                        //});
                        $linkedIn.profile().then(function(result) {
                            var firstResult = result.values[0];
                            $scope.stalker = {}
                            $scope.stalker.name = firstResult.firstName + ' ' + firstResult.lastName;
                            stalkerService.setLinkedInStalker(firstResult);
                            $scope.$emit('loggedInEvent', 'linkedIn');
                            $scope.stalker.picture = firstResult.pictureUrl;
                        });
                    } else {
                        console.log("LINKEDINCONTROLLER: Logged in and not authorized");
                    }
                });

            };

            this.logout = function() {
                if ($linkedIn.isAuthorized) {
                    $linkedIn.logout().then(function() {
                        console.log("LINKEDINCONTROLLER: Logged out");
                        controller.setPage($scope.pages.login);
                        stalkerService.setLinkedInLoggedIn(false);
                        $scope.$emit('loggedOutEvent', 'linkedIn');
                    });
                } else {
                    console.log("LINKEDINCONTROLLER: Already logged out");
                }
            };


            /* ------------------ Stalker LinkedIn views navigation ------------------ */

            $scope.$on('handleBroadcast', function() {
                $scope.victim = {};
                $scope.search = searchService.search;
                // controller.searchCall($scope.search.name, $scope.search.email);
            });

            var currentPage = $scope.pages.login;

            this.isSelected = function(checkPage) {
                return currentPage === checkPage;
            };

            this.setPage = function(selectPage) {
                currentPage = selectPage;
            };
        }
    ]);
});
