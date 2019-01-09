'use strict';

angular.module('uwoshApp', ['ngSanitize']);

// CONTROLLERS
angular.module('uwoshApp')
  .controller('EventsCtrl', ['$scope', '$http', function ($scope,$http) {
    $http.get('http://pipes.yahoo.com/pipes/pipe.run?_id=2FV68p9G3BGVbc7IdLq02Q&_render=json&feedcount=3&feedurl=http%3A%2F%2Fwww.uwosh.edu%2Ftoday%2Fevents%2Fcategory%2Fstudy-away-participants%2Ffeed%2F').success(function(data) {
      $scope.events = data.value.items;
    }).error(function() {
      // Some error occurred
    });
  }]);

// FILTERS
angular.module('uwoshApp')
  .filter('characters', function () {
    return function (input, chars, breakOnWord) {
      if (isNaN(chars)) {
        return input;
      }
      if (chars <= 0) {
        return '';
      }
      if (input && input.length >= chars) {
        input = input.substring(0, chars);

        if (!breakOnWord) {
          var lastspace = input.lastIndexOf(' ');
          //get last space
          if (lastspace !== -1) {
            input = input.substr(0, lastspace);
          }
        } else {
          while(input.charAt(input.length-1) === ' '){
            input = input.substr(0, input.length -1);
          }
        }
        return input + '...';
      }
      return input;
    };
  })
  .filter('cleanDate', function () {
    return function(dateString) {
      return moment(new Date(dateString)).format();
    };
  })
  .filter('fromNow', function () {
    return function(dateString) {
      return moment(dateString).fromNow();
    };
  })
  .filter('words', function () {
    return function (input, words) {
      if (isNaN(words)) {
        return input;
      }
      if (words <= 0) {
        return '';
      }
      if (input) {
        var inputWords = input.split(/\s+/);
        if (inputWords.length > words) {
          input = inputWords.slice(0, words).join(' ') + '...';
        }
      }
      return input;
    };
  })
  .filter('tweetLinky',['$filter',
    function($filter) {
      return function(text, target) {
        if (!text) return text;

        var replacedText = $filter('linky')(text, target);
        var targetAttr = "";
        if (angular.isDefined(target)) {
            targetAttr = ' target="' + target + '"';
        }
        // replace #hashtags and send them to twitter
        var replacePattern1 = /(^|\s)#(\w*[a-zA-Z_]+\w*)/gim;
        replacedText = text.replace(replacePattern1, '$1<a href="https://twitter.com/search?q=%23$2"' + targetAttr + '>#$2</a>');
        // replace @mentions but keep them to our site
        var replacePattern2 = /(^|\s)\@(\w*[a-zA-Z_]+\w*)/gim;
        replacedText = replacedText.replace(replacePattern2, '$1<a href="https://twitter.com/$2"' + targetAttr + '>@$2</a>');
        return replacedText;
      };
    }
  ]);
