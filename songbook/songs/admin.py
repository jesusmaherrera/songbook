#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Song, Tag

admin.site.register(Song)
admin.site.register(Tag)