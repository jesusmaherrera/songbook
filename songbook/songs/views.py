from django.views.generic import ListView, FormView, UpdateView, DetailView, CreateView
from django.shortcuts import render
from songs.models import Song
from songs.forms import SongForm


class SongDetailView(DetailView):
    model = Song
    template_name = 'song.html'

    def get_context_data(self, **kwargs):
        context = super(SongDetailView, self).get_context_data(**kwargs)
        context['formated_song'] = self.object.lyrics.replace('[','<strong class="tone">').replace(']','</strong>').replace('\r\n','<br/>')
        return context

class SongList(ListView):
	model = Song
	template_name = 'songs.html'

class SongFormView(CreateView):
	form_class = SongForm
	template_name = 'song.html'
	success_url = '/songs/'

class SongUpdate(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'song.html'
    success_url = '/songs/'

    def get_context_data(self, **kwargs):
        context = super(SongUpdate, self).get_context_data(**kwargs)
        context['formated_song'] = self.object.lyrics.replace('[','<strong class="tone">').replace(']','</strong>').replace('\r\n','<br/>')
        return context