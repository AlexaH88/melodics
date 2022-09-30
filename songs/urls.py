from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongList.as_view(), name='home'),
    path('<slug:slug>/', views.SongDetail.as_view(), name='song_detail'),
    path('add-song', views.AddSong.as_view(), name='add_song'),
]
