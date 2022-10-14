from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Song
from . forms import SongForm


class SongList(generic.ListView):
    model = Song
    queryset = Song.objects.order_by('artist')
    template_name = 'index.html'
    # paginate_by = 6


class SongDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Song.objects.filter()
        song = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "song_detail.html",
            {
                "song": song,
            },
        )


class AddSong(View):

    def get(self, request):

        return render(
            request,
            "add_song.html",
            {
                "song_form": SongForm(),
                "song_added": False
            },
        )

    def post(self, request):

        song_form = SongForm(data=request.POST)

        if song_form.is_valid():
            song_form.instance.uploaded_by = request.user
            song_form.save()
        else:
            song_form = SongForm()

        return render(
            request,
            "add_song.html",
            {
                "song_form": SongForm(),
                "song_added": True
            },
        )


class AccountDetail(View):

    def get(self, request, *args, **kwargs):

        model = User
        username = model.username
        email = model.email
        date_joined = model.date_joined
        last_login = model.last_login

        songs = Song.objects.all()
        # user_songs = Song.objects.order_by('uploaded_by')
        user_songs = Song.objects.filter(uploaded_by=request.user)

        return render(
            request,
            "account.html",
            {
                "username": username,
                "email": email,
                "date_joined": date_joined,
                "last_login": last_login,
                "songs": songs,
                "user_songs": user_songs,
            },
        )
