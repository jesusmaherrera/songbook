from django.forms import ModelForm, Textarea
from .models import Song
from django import forms


class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = ('name', 'lyrics',)
		widgets = {
            'lyrics': Textarea(attrs={'cols': 120, 'rows': 20}),
        }