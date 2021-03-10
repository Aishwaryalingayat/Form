var web_app = angular.module("webApp", []);

// controllers
web_app.controller('tickitingToolCtrl', function($scope, tickitingToolProjectList) {
    tickitingToolProjectList.initializeFunctions($scope);
});

// service
web_app.service('tickitingToolProjectList', function($http) {

    var serviceFunctions = {
        initializeFunctions: function($scope) {
            $scope.tickiting_tool_entry = {};
            // to get already added tikiting tools list
            $scope.getTickitingToolProjectList = function() {
                $http({
                    url : "/pro/api/get-tickiting-tools/",
                    method : "GET",
                }).then(function onSuccess(response) {
                    $scope.tickiting_tools = response.data.tools;
                }, function onError(response) {
                    $scope.myWelcome = response.statusText;
                });
            }
            $scope.getTickitingToolProjectList();

            // to add tikiting tool
            $scope.addTickitingTool = function() {
                $http({
                    url: "/pro/api/add-tickiting-tools/",
                    method: "POST",
                    data: $scope.tickiting_tool_entry
                }).then(function onSuccess(response) {
                    $scope.tickiting_tool_entry = {};
                    $scope.app_config.addEntry = false;
                    $scope.getTickitingToolProjectList();
                }, function onError(response) {
                    $scope.myWelcome = response.statusText;
                });
            }
        }
    };
    return serviceFunctions;
});