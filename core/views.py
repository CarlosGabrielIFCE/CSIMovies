from rest_framework import generics
from django.shortcuts import render
from .models import Film
from .serializers import FilmSerializer

class FilmList(generics.ListCreateAPIView):
    def get(self, request):
        films = Film.objects.all()
        serializer_class = FilmSerializer
        context = {
            'films': films,
        }
        return render(request, 'films.html', context)

    def get_film(self, request):
        film = Film.objects.filter(rt_score==8)
        return film.image.url
