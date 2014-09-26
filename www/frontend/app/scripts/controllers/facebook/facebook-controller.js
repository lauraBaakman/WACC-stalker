define(['../module'], function(controllers, ngFacebook) {
    'use strict';
    controllers.controller('FacebookController', ['$scope', '$facebook', 'searchService',
        function($scope, $facebook, searchService) {

            var controller = this;

            //  Provides 
            //      1. The Stalker API calls (So we got the backend communication in one place)
            //      2. Navigation between the Facebook panels: login, results, detail
            //      3. Besides the navigation the necessary FaceBook API calls for login and logout.
            //      4. ...

            // TODO: Maybe scope some of the duplicate function to a higher controller??? Inheritance? Or 
            // in a Service and let all the controller depend on them. (Better I think.)

            // NOTE: Dummy data
            var tmpResults = [{
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
            }];

            // NOTE: Dummy data
            var tmpPerson = {
                "id": "629307900522293",
                "first_name": "Rick",
                "last_name": "Van der Veen",
                "link": "https://www.facebook.com/app_scoped_user_id/629307900522293/",
                "name": "Rick Van der Veen",
                "updated_time": "2012-05-23T23:03:02+0000"
            };

            // Initialization data objects
            $scope.search = null;
            $scope.results = null;
            $scope.person = null;

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
                            controller.setPage($scope.pages.results);
                            console.log($facebook.getAuthResponse());
                        }
                    });
                });
            };

            this.logout = function() {
                $facebook.getLoginStatus().then(function(response) {
                    if (!(response.status === "unknown" || response.authResponse === null)) {
                        $facebook.logout();

                    }
                    controller.setPage($scope.pages.login);
                });
            };

            /* ------------------ Handle Search messages ------------------ */

            $scope.$on('handleBroadcast', function() {
                console.log("FACEBOOKCONTROLLER: Search message received");

                $scope.search = searchService.search;

                controller.searchCall($scope.search.name, $scope.search.email);
            });

            /* ------------------ Stalker API calls ------------------ */

            this.searchCall = function(name, email) {
                console.log("FACEBOOKCONTROLLER: Searching with: " + "Name: " + name + ", Email: " + email);

                // TODO: Check name and email

                // TODO: Stalker logic (API call, processing data)

                // Set (processed) API data in the scope.resultss
                $scope.results = tmpResults;

                // Set the view to the results page
                this.setPage($scope.pages.results);
            };

            this.detailsCall = function(id) {
                console.log("FACEBOOKCONTROLLER: Searching details of user with id: " + id);

                // TODO: Check Id

                // TODO: Stalker logic (API call, processing data)

                // TODO: Set (processed) API data in scope.person
                $scope.person = tmpPerson;

                // Set the view to the detail page
                this.setPage($scope.pages.detail);
            };


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
