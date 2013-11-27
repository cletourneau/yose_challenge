$('form').submit (event)->
  number = $('input#number').val()
  $.get("/primeFactors?number=#{number}", (data)->
    $('#result').html("#{data.number} = #{data.decomposition.join(' x ')}")
  )
  event.preventDefault()

