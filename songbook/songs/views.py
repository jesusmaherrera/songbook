# -*- coding: utf-8 -*-

from django.views.generic import ListView, FormView, UpdateView, DetailView, CreateView
from django.shortcuts import render
from songs.models import Song
from songs.forms import SongForm, SongListForm, SongListForm
from .forms import SongListItemFormSet

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'

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


class SongListUpdate(UpdateView):
    model = SongList
    form_class = SongListForm
    template_name = 'songs/songlist_form.html'
    success_url = '/songs/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SongListItemFormSet(instance = self.object)
        return self.render_to_response(self.get_context_data(form = form, formset = formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SongListItemFormSet(self.request.POST, instance=self.object)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class SongListCreate(CreateView):
    model = SongList
    form_class = SongListForm
    template_name = 'songs/songlist_form.html'
    success_url = '/songs/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SongListItemFormSet()
        return self.render_to_response(self.get_context_data(form=form,formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SongListItemFormSet(self.request.POST)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form,formset=formset))
