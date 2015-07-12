from django.views.generic import ListView, FormView, UpdateView, DetailView, CreateView
from django.shortcuts import render
from songs.models import Song
from songs.forms import SongForm


class SongDetailView(DetailView):
    model = Song
    template_name = 'song.html'

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
