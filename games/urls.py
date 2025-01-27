from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games_list, name='games_list'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('stats/', views.stats_view, name='stats'),
]
