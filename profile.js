// It is important that the app name is c_ajsApp
var c_ajsApp = angular.module('c_ajsView', ['chart.js']);
c_ajsApp.controller('c_ajsCtrl', function($sce, $scope, $http) {

    $http.get("locIndex.json").then(function(dataJSON) {
        $scope.data =  dataJSON.data;
    });

    $scope.urlencode = function(string){
        string = string.replace(' ', '%20');
        return string;
    };

    $scope.trustAsResourceUrl = $sce.trustAsResourceUrl;



});
