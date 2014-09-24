define(['./module'], function (services) {
    'use strict';
    services.service('searchService', ['$rootScope', function ($rootScope) {
    	return {
    		search: {
    			"name": "",
    			"email": ""
    		},

    		broadcast: function (search) {
    			this.search = search;
    			this.send();
    		},

    		send: function() {
    			$rootScope.$broadcast('handleBroadcast');
    			console.log("Send message!");
    		}
    	};
    }]);
});