from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('films/', views.FilmList.as_view(), name='films-list'),
]
