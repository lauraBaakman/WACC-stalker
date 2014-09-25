/**
 * loads sub modules and wraps them up into the main module
 * this should be used for top-level module definitions only
 */
define([
    'angular',
    'angular-route',
    'jquery',
    'angular-facebook',
    './controllers/index',
    './directives/index',
    './filters/index',
    './services/index'
], function(angular) {
    'use strict';

    return angular.module('app', [
        'ngFacebook',
        'app.controllers',
        'app.directives',
        'app.filters',
        'app.services',
        'ngRoute'
    ]).config(function($facebookProvider) {
        $facebookProvider.setAppId('717667088304140');

        $facebookProvider.setCustomInit({
            version: 'v2.1',
            xfbml: false,
        });
    }).run(function($rootScope) {
        (function() {
            // If we've already installed the SDK, we're done
            if (document.getElementById('facebook-jssdk')) {
                return;
            }
            // Get the first script element, which we'll use to find the parent node
            var firstScriptElement = document.getElementsByTagName('script')[0];

            // Create a new script element and set its id
            var facebookJS = document.createElement('script');
            facebookJS.id = 'facebook-jssdk';

            // Set the new script's source to the source of the Facebook JS SDK
            facebookJS.src = '//connect.facebook.net/en_US/all.js';

            // Insert the Facebook JS SDK into the DOM
            firstScriptElement.parentNode.insertBefore(facebookJS, firstScriptElement);
        }());
    });
});
