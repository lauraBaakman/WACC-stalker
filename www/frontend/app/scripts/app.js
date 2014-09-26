/**
 * loads sub modules and wraps them up into the main module
 * this should be used for top-level module definitions only
 */
define([
    'angular',
    'angular-route',
    'angular-facebook',
    'angular-linkedin',
    'jquery',
    './controllers/index',
    './directives/index',
    './filters/index',
    './services/index'
], function(angular) {
    'use strict';

    return angular.module('app', [
        'ngFacebook',
        'ngLinkedIn',
        'app.controllers',
        'app.directives',
        'app.filters',
        'app.services',
        'ngRoute'
    ]).config(function($facebookProvider, $linkedInProvider) {
        $facebookProvider.setAppId('717667088304140');

        $facebookProvider.setCustomInit({
            version: 'v2.1',
            xfbml: false,
        });

        $linkedInProvider.set('appKey', '77h66s31h2but3');
    });
});
