// For any third party dependencies, like jQuery, place them in the lib folder.

// Configure loading modules from the lib directory,
// except for 'app' ones, which are in a sibling
// directory.
requirejs.config({
    baseUrl: 'js/lib',
    // Paths are from baseUrl e.g. js/lib/../app
    paths: {
        app: '../app',
        jquery: 'jquery-1.11.1',
        bootstrap: 'bootstrap'
    },
    shim: {
    	'bootstrap': {
    		deps: ['jquery']
    	}
    }

});

// Start loading the main app file. Put all of
// your application logic in there.
requirejs(['jquery', 'bootstrap', 'app/main']);
