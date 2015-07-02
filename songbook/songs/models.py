from django.db import models

class Song(models.Model):
    name = models.CharField('Nombre', max_length=200)
    lyrics = models.TextField('Contenido')