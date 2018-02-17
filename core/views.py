from rest_framework import generics
from django.shortcuts import render
from .models import Film, Serie
from .serializers import FilmSerializer
from .forms import Contact

class FilmList(generics.ListCreateAPIView):
    def get(self, request):
        series = Serie.objects.all()
        films = Film.objects.all()
        serie = Serie.objects.get(pk=3)
        film = Film.objects.get(pk=17)
        serializer_class = FilmSerializer
        context = {
            'film': film,
            'serie': serie,
            'films': films,
            'series': series,
        }
        return render(request, 'films.html', context)
