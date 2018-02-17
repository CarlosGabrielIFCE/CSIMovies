from rest_framework import generics
from django.shortcuts import render
from .models import Film, Serie
from .serializers import FilmSerializer


class FilmList(generics.ListCreateAPIView):
    def get(self, request):
        series = Serie.objects.all()
        films = Film.objects.all()
        serie = Serie.objects.get(pk=3)
        film = Film.objects.get(pk=17)
        film2 = Film.objects.get(pk=18)
        film3 = Film.objects.get(pk=19)
        film4 = Film.objects.get(pk=20)
        serializer_class = FilmSerializer
        context = {
            'film': film,
            'film2': film2,
            'film3': film3,
            'film4': film4,
            'serie': serie,
            'films': films,
            'series': series,
        }
        return render(request, 'films.html', context)
