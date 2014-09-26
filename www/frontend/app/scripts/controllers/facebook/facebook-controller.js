define(['../module'], function(controllers, ngFacebook) {
    'use strict';
    controllers.controller('FacebookController', ['$scope', '$facebook', 'searchService', 'stalkerService',
        function($scope, $facebook, searchService, stalkerService) {

            var controller = this;

            //  Provides 
            //      1. The Stalker API calls (So we got the backend communication in one place)
            //      2. Navigation between the Facebook panels: login, results, detail
            //      3. Besides the navigation the necessary FaceBook API calls for login and logout.
            //      4. ...

            // TODO: Maybe scope some of the duplicate function to a higher controller??? Inheritance? Or 
            // in a Service and let all the controller depend on them. (Better I think.)

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

            /* ------------------ Facebook API calls ------------------ */

            this.login = function() {
                $facebook.login().then(function() {
                    $facebook.getLoginStatus().then(function(response) {
                        if (response.status === "unknown" || response.authResponse === null) {
                            console.log("FACEBOOKCONTROLLER: Logged in unsuccessful");
                        } else {
                            console.log("FACEBOOKCONTROLLER: Logged in successful.");
                            $facebook.api("/me").then(function(result){
                                // If no result do something....
                                console.log(result)
                                $scope.user = result.name;
                                stalkerService.setFacebookStalker(result);
                            });
                            //controller.setPage($scope.pages.results);
                        }
                    });
                });
            };

            this.logout = function() {
                $facebook.getLoginStatus().then(function(response) {
                    if (!(response.status === "unknown" || response.authResponse === null)) {
                        $facebook.logout();

                    }
                    controller.clearResults();
                    controller.clearPerson();
                    $scope.user = null; // Functie?
                    controller.setPage($scope.pages.login);
                });
            };

            /* ------------------ Search API calls ------------------ */

            this.searchCall = function(name, email) {
                console.log("FACEBOOKCONTROLLER: Searching with: " + "Name: " + name + ", Email: " + email);
                this.clearResults();
                this.clearPerson();

                $facebook.api("/search?q='" + name + "'&type=user").then(function(results) {
                    $scope.results = results.data;
                    controller.setPage($scope.pages.results);
                });
            };

            this.detailsCall = function(id) {
                console.log("FACEBOOKCONTROLLER: Searching details of user with id: " + id);
                $facebook.api("/" + id ).then(function(details) {
                    $scope.person = details;
                    $facebook.api("/" + id + "/picture").then(function(picture) { 
                        $scope.person.picture = picture.data.url;
                    });
                    controller.setPage($scope.pages.detail);
                });

            };


            /* ------------------ Handle Search messages ------------------ */

            $scope.$on('handleBroadcast', function() {
                console.log("FACEBOOKCONTROLLER: Search message received");

                $scope.search = searchService.search;

                controller.searchCall($scope.search.name, $scope.search.email);
            });

            /* ------------------ Stalker Facebook views navigation ------------------ */

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
