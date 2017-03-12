from django.db import models

class Song(models.Model):
    name = models.CharField('Titulo', max_length=200)
    lyrics = models.TextField('Contenido')
    lyrics_edit_view = models.TextField('Edicion')
    lyrics_formated = models.TextField('Contenido HTML')

    def __str__(self):
        return u'%s'% self.name

class Tag(models.Model):
    name = models.CharField('Nombre', max_length=200)
    song = models.ManyToManyField('Song')

    def __str__(self):
        return u'%s'% self.name