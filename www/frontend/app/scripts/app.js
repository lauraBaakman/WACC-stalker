define(['angular', 'controllers/controllers', 
	'services/services', 'filters/filters', 
	'directives/directives'], 
	function (angular) {
		return angular.module('stalker', ['controllers', 'services', 'filters', 'directives']);
	}
);