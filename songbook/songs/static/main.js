$(".tone").each(function( ) {
  var wi = $(this).width()
  var wid = (-48*wi/100)+"px"
  $(this).css({"margin":wid})
})