// Generated by CoffeeScript 1.6.3
(function() {
  $('form').submit(function(event) {
    var number;
    number = $('input#number').val();
    $.get("/primeFactors?number=" + number, function(data) {
      return $('#result').html("" + data.number + " = " + (data.decomposition.join(' x ')));
    });
    return event.preventDefault();
  });

}).call(this);