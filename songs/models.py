from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.TextField(max_length=200)
    album = models.TextField(max_length=200)
    lyrics = models.TextField()
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='song'
        )

    class Meta:
        ordering = ['artist']

    def __str__(self):
        return self.title
