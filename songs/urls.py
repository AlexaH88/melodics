from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongList.as_view(), name='home'),
    path('<slug:slug>/', views.SongDetail.as_view(), name='song_detail'),
]
