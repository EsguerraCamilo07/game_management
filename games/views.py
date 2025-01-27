from django.shortcuts import get_object_or_404
from .models import Game, Event, generate_unique_code
from django.http import HttpResponse
from django.contrib import messages
from .forms import JuegoForm
from django.shortcuts import render, redirect
from .models import Game
from django.http import HttpResponseForbidden

def index(request):
    return HttpResponse("<h1>Bienvenido al Sistema de Gestión de Juegos</h1>")

def index(request):
    return render(request, 'games/index.html')

def game_listar(request):
    titulo = "Listado de Juegos"
    juegos = Game.objects.all()  # Obtenemos todos los juegos

    context = {
        "titulo": titulo,
        "juegos": juegos
    }
    return render(request, "games/games_list.html", context)
def game_crear(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Juego creado exitosamente.")
            return redirect('games_list')
    else:
        form = JuegoForm()
    return render(request, 'games/crear.html', {'form': form, 'titulo': 'Nuevo Juego'})


def game_edit(request, id):
    juego = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('games_list')
    else:
        form = JuegoForm(instance=juego)

    return render(request, 'games/modificar.html', {'form': form, 'titulo': 'Modificar Juego'})


def game_delete(request, id):
    juego = get_object_or_404(Game, id=id)

    if request.method == 'POST':
        # Realizar la eliminación
        juego.delete()
        return redirect('games_list')  # Redirigir a la lista de juegos o la página que desees

    return HttpResponseForbidden()  # Si no es POST, no debería eliminar


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

