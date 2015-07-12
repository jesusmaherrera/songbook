var htmlOriginal = $.fn.html;

// redefine the `.html()` function to accept a callback
$.fn.html = function(html,callback){
  // run the old `.html()` function with the first parameter
  var ret = htmlOriginal.apply(this, arguments);
  // run the callback (if it is defined)
  if(typeof callback == "function"){
    callback();
  }
  // make sure chaining is not broken
  return ret;
}

$("#id_lyrics").change(function(){
	var lyrics_formated = $("#id_lyrics").val().replace(/\[/gi, '<strong class="tone">').replace(/\]/gi, '</strong>').replace(/\r\n|\r|\n/g,"<br />")
	$("p.lyrics_formated").html(lyrics_formated, function(){
		$(".vista_btn").trigger("click")
		$(".tone").each(function( ) {
		  var wi = $(this).width()
		  var wid = (-48*wi/100)+"px"
		  $(this).css({"margin":wid})
		})
		$("#id_lyrics_formated").val($("p.lyrics_formated").html())
	})


})
