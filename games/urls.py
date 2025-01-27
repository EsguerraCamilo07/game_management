from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('stats/', views.stats_view, name='stats'),
    path('games/', views.game_listar, name='games_list'),  # Vista de listado
    path('games/crear/', views.game_crear, name="juego_crear"),  # Vista de creación
    path('game/modificar/<int:id>/', views.game_edit, name='juego_modificar'),  # Vista para modificar


    path('game/eliminar/<int:id>/', views.game_delete, name='juego_eliminar'),  # Vista para eliminar
]
