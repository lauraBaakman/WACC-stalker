/**
 * loads sub modules and wraps them up into the main module
 * this should be used for top-level module definitions only
 */
define([
    'angular',
    'angular-route',
    'angular-facebook',
    'angular-linkedin',
    'angular-mdFive',
    'angular-http-loader',
    'bootstrap-ui',
    'jquery',
    'fs-dangle',
    './controllers/index',
    './directives/index',
    './filters/index',
    './services/index'
], function(angular) {
    'use strict';

    return angular.module('app', [
    	'ng.httpLoader',
        'ngFacebook',
        'ngLinkedIn',
        'ngMd5',
        'dangle',
        'ui.bootstrap',
        'app.controllers',
        'app.directives',
        'app.filters',
        'app.services',
        'ngRoute'
    ]).config(function($facebookProvider, $linkedInProvider, httpMethodInterceptorProvider) {
    	httpMethodInterceptorProvider.whitelistDomain('facebook.com');
    	httpMethodInterceptorProvider.whitelistDomain('linkedin.com');
        $facebookProvider.setAppId('717667088304140');
        $facebookProvider.setCustomInit({
            version: 'v2.1',
            xfbml: false
        });
        $facebookProvider.setPermissions("user_birthday,user_relationship_details");

        $linkedInProvider.set('appKey', '77h66s31h2but3');
    });
});
