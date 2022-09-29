from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongList.as_view(), name='home')
]
