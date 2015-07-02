from django.shortcuts import render
from django.views.generic import DetailView
from songs.models import Song

class SongDetailView(DetailView):
    model = Song
    template_name = 'song.html'

    def get_context_data(self, **kwargs):
        context = super(SongDetailView, self).get_context_data(**kwargs)
        context['formated_song'] = self.object.lyrics.replace('[','<strong class="tone">').replace(']','</strong>').replace('\r\n','<br/>')
        return context