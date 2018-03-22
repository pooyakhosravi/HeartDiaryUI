angular.module("app", ["chart.js"]).controller("LineCtrl", function ($scope, $http) {

    $http.get("data.json").then(function(dataJSON) {
        $scope.alldata =  dataJSON.data;
        $scope.mydate = '0210_2018';
        $scope.dates = [];

        for(var k in $scope.alldata['heartrate']){
            console.log(k);
            $scope.dates.push(k);
        }

        $scope.ddata = $scope.alldata['heartrate'][$scope.mydate]['rates'];
        $scope.data= [];
        $scope.labels=[];
        $scope.makeArray($scope.ddata);
    });

    $scope.makeArray = function(myjson){
        $scope.data= [];
        $scope.labels=[];
        for(var k in myjson){
            console.log(k);
            $scope.labels.push(k);
            $scope.data.push(myjson[k]);
        }
    };

    $scope.changeDate = function(date){
        $scope.mydate = date;
        $scope.ddata = $scope.alldata['heartrate'][$scope.mydate]['rates'];

        $scope.makeArray($scope.ddata);
        return date;
    };

    //$scope.labels = ["Download Sales", "In-Store Sales", "Mail-Order Sales", "Tele Sales", "Corporate Sales"];
    //$scope.data = [300, 500, 100, 40, 120];
    //$scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
    $scope.series = ['Series A'];
    // $scope.data = [
    //   [65, 59, 80, 81, 56, 55, 40],
    //   [28, 48, 40, 19, 86, 27, 90]
    // ];
    $scope.onClick = function (points, evt) {
      console.log(points, evt);
    };
    $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
    $scope.options = {
      scales: {
        yAxes: [
          {
            id: 'y-axis-1',
            type: 'linear',
            display: true,
            position: 'left'
          }
        ]
      }
    };
  });