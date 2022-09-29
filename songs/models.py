from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.TextField(max_length=200)
    album = models.TextField(max_length=200)
    lyrics = models.TextField()

    class Meta:
        ordering = ['artist']

    def __str__(self):
        return self.title
