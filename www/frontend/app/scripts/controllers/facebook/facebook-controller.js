define(['../module'], function(controllers, ngFacebook) {
    'use strict';
    controllers.controller('FacebookController', ['$scope', '$facebook', 'searchService', 'stalkerService', 'apiService',
        function($scope, $facebook, searchService, stalkerService, apiService) {

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
            $scope.error = null;
            this.victim = null;

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

            this.hasError = function() {
            	return ($scope.error !== null);
            }

            this.clearResults = function() {
                $scope.results = null;
            };

            this.clearPerson = function() {
                $scope.person = null;
            };

            this.clearError = function(){
            	$scope.error = null;
            }

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
                                $scope.stalker = {};
                                $scope.stalker.name = result.name;
                                stalkerService.setFacebookStalker(result);
                                $scope.$emit('loggedInEvent', 'facebook');
                                $facebook.api("/" + result.id + "/picture").then(function(picture) { 
                                    console.log(picture.data.url);
                                    $scope.stalker.picture = picture.data.url;
                                });
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
                    stalkerService.setFacebookLoggedIn(false);
                    $scope.$emit('loggedOutEvent', 'facebook');
                    // controller.clearResults();
                    // controller.clearPerson();
                    // $scope.user = null; // Functie?
                    // controller.setPage($scope.pages.login);
                });
            };

            /* ------------------ Search API calls ------------------ */

            this.searchCall = function(name, email) {
            	$scope.loading = true;
                console.log("FACEBOOKCONTROLLER: Searching with: " + "Name: " + name + ", Email: " + email);
                this.clearResults();
                this.clearPerson();
                this.clearError();

                $facebook.api("/search?q='" + name + "'&type=user").
                	then(
						function(results) {
	                    	$scope.results = results.data;
	                    	controller.setPage($scope.pages.results);
	                    	$scope.loading = false;
	                	}, 
	                	function(reason){
	                		$scope.error = "Some error occurred."
	                		$scope.loading = false;
	                	}
                	);
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

            this.setVictim = function(id){
                // post victim
                var victim = {
                    victim_id : id
                };
                apiService.postVictim(victim).then(
                    function(){
                        console.log('posted victim');
                        if(this.victim){
                            $('#' + this.victim.victim_id).removeClass('success');
                        }
                        this.victim = victim;
                        $('#' + this.victim.victim_id).addClass('success');
                        // search_id = get search id
                        // apiService.putSearch()
                        // update the class of the button of the current victim
                    }, 
                    function(){
                        $scope.error = "Something went wrong, your victim has not been stored.";
                    });
            }


            /* ------------------ Handle Search messages ------------------ */

            $scope.$on('handleBroadcast', function() {
                $scope.victim = {};
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
