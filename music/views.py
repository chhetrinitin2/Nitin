from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html',{'all_albums':all_albums})
def folder(request):
    hello manaa


def detail(request, album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("album doesn't exist")
    return render(request, 'music/detail.html', {'album':album})
