from django.forms import ModelForm, Textarea, HiddenInput
from .models import Song
from django import forms


class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = ('name', 'lyrics','lyrics_formated')
		widgets = {
            'lyrics': Textarea(attrs={'cols': 120, 'rows': 20}),
            'lyrics_formated': HiddenInput(),
        }