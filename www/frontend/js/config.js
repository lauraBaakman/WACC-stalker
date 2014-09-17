// For any third party dependencies, like jQuery, place them in the lib folder.

// Configure loading modules from the lib directory,
// except for 'app' ones, which are in a sibling
// directory.
requirejs.config({
    baseUrl: 'js/lib',
    // Paths are relative to baseUrl e.g. js/lib/../app
    paths: {
        app: '../app',
        jquery: 'jquery-1.11.1',
        bootstrap: 'bootstrap',
        angular: 'angular'
    },
    shim: {
    	'bootstrap': {
    		deps: ['jquery']
    	}
    }

});

// Start loading the main app file. Put all of
// your application logic in there.
requirejs(['angular', 'jquery', 'bootstrap', 'app/main']);
