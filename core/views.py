from rest_framework import generics
from django.shortcuts import render
from .models import Film, Serie
from .serializers import FilmSerializer
from .forms import Contact

class FilmList(generics.ListCreateAPIView):
    def get(self, request):
        success = False
        if request.method == "POST":
            form = Contact(request.POST)
            if form.is_valid():
                form.send_mail()
                form = Contact()
                success = True
        else:
            form = Contact()
        series = Serie.objects.all()
        films = Film.objects.all()
        serializer_class = FilmSerializer
        context = {
            'form': form,
            'films': films,
            'series': series,
        }
        return render(request, 'films.html', context)
