define(['./module'], function(services) {
    'use strict';
    services.service('stalkerService', ['md5', '$rootScope', '$facebook', '$linkedIn',
        function(md5, $rootScope, $facebook, $linkedIn) {
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
                    this.loggedIn.facebook = true;
                },

                setLinkedInStalker: function(data) {
                    this.stalker.linkedInId = md5.createHash(data.id);
                    this.stalker.industry = data.industry;
                    this.linkedIn.facebook = true;
                },

                isLoggedIn: function() {
                    return this.loggedIn.facebook || this.loggedIn.linkedIn;
                }
            };
        }
    ]);
});
