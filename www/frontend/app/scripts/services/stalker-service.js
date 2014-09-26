define(['./module'], function (services) {
    'use strict';
    services.service('stalkerService', ['$rootScope', function ($rootScope) {
    	return {
    		stalker: {
                facebookId: null,
                linkedInId: null,
                relatie: null,
                birthdate: null,
                gender: null,
                industry: null
            },

            setFacebookStalker: function(data) {
                stalker.facebookId = data.iets;
                
            }
    	};
    }]);
});
