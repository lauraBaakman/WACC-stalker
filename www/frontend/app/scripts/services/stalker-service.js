define(['./module'], function(services) {
    'use strict';
    services.service('stalkerService', ['md5', '$rootScope', '$facebook', '$linkedIn', 'apiService',
        function(md5, $rootScope, $facebook, $linkedIn, apiService) {
            return {
                stalker: {
                    facebookId: null,
                    linkedInId: null,
                    relationship: null,
                    birthdate: null,
                    gender: null,
                    industry: null
                },

                loggedIn: {
                    facebook: false,
                    linkedIn: false
                },

                setFacebookStalker: function(data) {
                    this.stalker.facebookId = md5.createHash(data.id);
                    this.stalker.gender = data.gender;
                    this.stalker.realtionship = data.relationship;
                    this.stalker.birthdate = data.birthday;
                    this.stalker.relationship = data.relationship_status;
                    this.setFacebookLoggedIn(true);
                },

                setFacebookLoggedIn: function(bool) {
                    this.loggedIn.facebook = bool;
                },

                setLinkedInStalker: function(data) {
                    this.stalker.linkedInId = md5.createHash(data.id);
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
                    console.log('commitStalker');
                }
            };
        }
    ]);
});
