from django.forms import ModelForm, Textarea, HiddenInput
from django.forms import inlineformset_factory

from .models import Song, SongListItem, SongList
from django import forms

class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = ('name', 'lyrics','lyrics_formated','lyrics_edit_view')
		widgets = {
            'lyrics': HiddenInput(),
            'lyrics_edit_view': Textarea(attrs={'cols': 120, 'rows': 20, 'style':'font-family:courier',}),
            'lyrics_formated': HiddenInput(),
        }

class SongListItemForm(ModelForm):
	class Meta:
		model = SongListItem
		fields = ('song',)

class SongListForm(ModelForm):
	class Meta:
		model = SongList
		fields = ('name',)


SongListItemFormSet = inlineformset_factory(SongList, SongListItem, form=SongListItemForm, extra=1, fields=('song',))