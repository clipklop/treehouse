angular.module('todoListApp')
.directive('helloWorld', function() {
  return {
    template: 'That is hello world directive!',
    restrict: 'E'
  }
})