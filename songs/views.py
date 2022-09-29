from django.shortcuts import render
from django.views import generic
from .models import Song


class SongList(generic.ListView):
    model = Song
    queryset = Song.objects.order_by('artist')
    template_name = 'index.html'
    paginate_by = 6
