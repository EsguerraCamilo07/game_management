from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Rutas para el admin
    path('', include('games.urls')),  # Rutas de la aplicación "games"
]
