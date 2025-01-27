from django.shortcuts import render
from .models import Game, Event
from django.http import JsonResponse
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Bienvenido al Sistema de Gestión de Juegos</h1>")

def index(request):
    return render(request, 'games/index.html')

def games_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'games/calendar.html', {'events': events})

def stats_view(request):
    stats = Game.objects.all()
    stats_data = [
        {"name": game.name, "rentals": Event.objects.filter(game=game).count()}
        for game in stats
    ]
    return render(request, 'games/stats.html', {'stats': stats_data})
