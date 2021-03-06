/**
 * bootstraps angular onto the window.document node
 * NOTE: the ng-app attribute should not be on the index.html when using ng.bootstrap
 */
define([
    'require',
    'angular',
    'app',
    'routes'
], function (require, ng) {
    'use strict';

    /*
     * place operations that need to initialize prior to app start here
     * using the `run` function on the top-level module
     */

     // TODO: Move
     String.prototype.isEmpty = function() {
        return (this.length === 0 || !this.trim());
     };

    require(['domReady!'], function (document) {
        ng.bootstrap(document, ['app']);
    });
});
