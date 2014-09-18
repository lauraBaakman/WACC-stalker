// For any third party dependencies, like jQuery, place them in the lib folder.

// Configure loading modules from the lib directory,
// except for 'app' ones, which are in a sibling
// directory.
requirejs.config({
    paths: {
        angular: 'vendor/angular.min',
        jquery: 'vendor/jquery-1.11.1',
        bootstrap: 'vendor/bootstrap',
        domReady: 'vendor/domReady'
    },
    shim: {
        angular: {
            deps: ['jquery'],
            exports: 'angular'
        },
    	bootstrap: {
    		deps: ['jquery']
    	}
    }

});

// Start loading the main app file. Put all of
// your application logic in there.
requirejs(['angular', 'jquery', 'bootstrap', 'domReady']);
