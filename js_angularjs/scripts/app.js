angular.module("todoListApp", [])
.controller('mainCtrl', function($scope, dataService) {
  $scope.helloConsole = dataService.helloConsole;
  $scope.helloWorld = function(){
    console.log("Hi, there, This is the helloWorld Controller, and it's alive!")
  }
  
  $scope.ngChange = function() {
    console.log('Value has changed.')
  }

  dataService.getTodos(function(response) {
      console.log(response.data)
      $scope.todos = response.data
    })

  $scope.deleteTodo = function(todo) {
    dataService.deleteTodo(todo)
  }
})
.controller('coolCtrl', function ($scope) {
  $scope.whoAmI = function () {
    console.log("Yo, Final countdown. It's a coolCtrl here!")
  };

  $scope.helloWorld = function () {
    console.log("Thats not what you wanted.")
  }
})
.controller('imASibling', function($scope) {
  $scope.foobar = 1234;
})
.service('dataService', function($http) {
  this.helloConsole = function() {
    console.log("Say Hi, from the service!")
  }
  this.getTodos = function(callback) {
    $http.get('mock/todos.json')
    .then(callback)
  }

  this.deleteTodo = function(todo) {
    console.log(`The ${todo.name} has been deleted!`)
  }
  this.saveTodo = function(todo) {
    console.log(`The ${todo.name} has been saved!`)
  }
});