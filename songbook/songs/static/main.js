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
$("#id_lyrics_edit_view").change(function(){
	var lines = $("#id_lyrics_edit_view").val().split(/\n/)
	var new_lines = ''
	var notes_line = ''
	var new_line = ''
	var lyrics  = ''
	var notes = []
	lines.forEach(function(line){ 
		// Es una linea con notes musicales
		if( line.indexOf('  ') != -1 ){
			notes_line = line
		}else if (notes_line != ''){
			new_line = line
			// Recorremos la linea de notes
			var note = ''
			var notes_dic = []
			var notes_line_length = notes_line.length-1
			for(index in notes_line){
				// debugger
				if(notes_line[index]!=' '){
					note += notes_line[index]
					// Si es la ultima letra y no es espacio
					if (index == notes_line_length && note !=''){
						notes.push(note)
						note = ''	
					}
				}else if(note != ''){
					notes.push(note)
					note = ''
				}
			}

			// Sacar los indices de cada nota
			var last_note_index = 0
			var notas_length = 0
			for (index in notes){
				note_index = notes_line.indexOf(notes[index], last_note_index)
				last_note_index =  note_index + notes[index].length
				notas_length += notes[index].length
				notes_dic.push({
					'note':notes[index],
					'index':note_index+1
				})
			}

			notes = []

			var extra_characters = 0

			for( index in notes_dic){
				note = notes_dic[index]
				new_index = note.index + extra_characters
				new_line = new_line.slice(0,new_index) + '['+ note.note +']'+new_line.slice(new_index)
				extra_characters += note.note.length + 2
			}
			new_lines += new_line + '\n'
			notes_line = ''
		}else{
			new_lines += line + '\n'
		}
	})

	$("#id_lyrics").val(new_lines)
	$("#id_lyrics").trigger('change')
})


