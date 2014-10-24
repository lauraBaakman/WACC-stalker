define(['./module'], function(services) {
    'use strict';
    services.service('stalkerService', ['md5', '$rootScope', '$facebook', '$linkedIn', 'apiService',
        function(md5, $rootScope, $facebook, $linkedIn, apiService) {
            return {
                stalker: {
                    stalker_id: null, // = facebook id
                    linkedIn_id: null,
                    relationship_status: null,
                    birthdate: null,
                    gender: null,
                    industry: null
                },

                loggedIn: {
                    facebook: false,
                    linkedIn: false
                },

                setFacebookStalker: function(data) {
                    this.stalker.stalker_id = md5.createHash(data.id);
                    this.stalker.gender = data.gender;
                    this.stalker.relationship_status = data.relationship_status;
                    this.stalker.birthdate = data.birthday;
                    this.setFacebookLoggedIn(true);
                },

                setFacebookLoggedIn: function(bool) {
                    this.loggedIn.facebook = bool;
                },

                setLinkedInStalker: function(data) {
                    this.stalker.linkedIn_id = md5.createHash(data.id);
                    this.stalker.industry = data.industry;
                    this.setLinkedInLoggedIn(true);
                },

                setLinkedInLoggedIn: function(bool) {
                    this.loggedIn.linkedIn = bool;
                },                

                isLoggedIn: function() {
                    return this.loggedIn.facebook || this.loggedIn.linkedIn;
                },

                commitStalker: function() {
                    apiService.postStalker(this.stalker).then(
                        function(result){
                            console.log(result);
                        },
                        function(error){
                            console.log(error);
                        });
                }
            };
        }
    ]);
});