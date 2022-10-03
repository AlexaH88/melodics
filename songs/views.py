from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Song
from . forms import SongForm


class SongList(generic.ListView):
    model = Song
    queryset = Song.objects.order_by('artist')
    template_name = 'index.html'
    paginate_by = 6


class SongDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Song.objects.filter()
        song = get_object_or_404(queryset, slug=slug)
        artist = song.artist
        album = song.album
        lyrics = song.lyrics

        return render(
            request,
            "song_detail.html",
            {
                "song": song,
                "artist": artist,
                "album": album,
                "lyrics": lyrics,
            },
        )


class AddSong(View):

    def get(self, request):

        return render(
            request,
            "add_song.html",
            {
                "song_form": SongForm()
            },
        )

    def post(self, request):

        song_form = SongForm(data=request.POST)

        if song_form.is_valid():
            song_form.instance.email = request.user.email
            song_form.instance.name = request.user.username
            song_form.save()
        else:
            song_form = SongForm()

        return render(
            request,
            "add_song.html",
            {
                "song_form": SongForm()
            },
        )
