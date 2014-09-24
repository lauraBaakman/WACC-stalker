/**
 * configure RequireJS
 * prefer named modules to long paths, especially for version mgt
 * or 3rd party libraries
 */
require.config({

    paths: {
        'angular': '../vendor/angular/angular',
        'angular-route': '../vendor/angular-route/angular-route',
        'domReady': '../vendor/requirejs-domready/domReady',
        'jquery': '../vendor/jquery/jquery-1.11.1',
        'bootstrap-ui': '../vendor/angular-ui/ui-bootstrap-custom-tpls-0.10.0'
    },

    /**
     * for libs that either do not support AMD out of the box, or
     * require some fine tuning to dependency mgt'
     */
    shim: {
        'angular': {
            exports: 'angular',
            deps: ['jquery']
        },
        'angular-route': {
            deps: ['angular']
        },
        'bootstrap-ui': {
            deps: ['angular']
        }
    },
    deps: [
        // kick start application... see bootstrap.js
        './bootstrap'
    ]
});
