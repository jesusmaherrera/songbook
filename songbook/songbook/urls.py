"""songbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from songs.views import SongDetailView, SongList, SongFormView, SongUpdate, SongListUpdate, SongListCreate
urlpatterns = [
	url(r'^$', SongList.as_view(), name='song-list'),
	url(r'^songs/$', SongList.as_view(), name='song-list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^song/$', SongFormView.as_view(), name='song-form'),
    url(r'^song/edit/(?P<pk>[-\w]+)/', SongUpdate.as_view(), name='song-form'),
    url(r'^song/(?P<pk>[-\w]+)/$', SongDetailView.as_view(), name='song-detail'),

    url(r'^songlist/edit/(?P<pk>[-\w]+)/', SongListUpdate.as_view(), name='songlist-update'),
    url(r'^songlist/$', SongListCreate.as_view(), name='songlist-create'),

]
