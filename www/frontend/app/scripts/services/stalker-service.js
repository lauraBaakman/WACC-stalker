define(['./module'], function (services) {
    'use strict';
    services.service('stalkerService', ['md5', '$rootScope', function (md5, $rootScope) {
    	return {
    		stalker: {
                facebookId: null,
                linkedInId: null,
                relationship: null,
                birthdate: null,
                gender: null,
                industry: null
            },

            setFacebookStalker: function(data) {
                this.stalker.facebookId = md5.createHash(data.id);
                this.stalker.gender = data.gender;
                this.stalker.realtionship = data.relationship;
                this.stalker.birthdate = data.birthday;
                this.stalker.relationship = data.relationship_status;
            },

            setLinkedInStalker: function(data) {
                this.stalker.linkedInId = md5.createHash(data.id);
                this.stalker.industry = data.industry;
                console.log(this.stalker);
            }
    	};
    }]);
});
