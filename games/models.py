import random
from django.db import models

def generate_unique_code():
    """Genera un código único de 5 dígitos verificando su unicidad en la base de datos."""
    while True:
        code = str(random.randint(10000, 99999))
        if not Game.objects.filter(code=code).exists():
            return code

class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Juego")
    category = models.CharField(max_length=50, default="General", verbose_name="Categoría")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    code = models.CharField(
        max_length=5, 
        unique=True, 
        default=generate_unique_code, 
        verbose_name="Código Único"
    )
    available = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return f"{self.name} - {self.code}"

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"

    


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.game.name} - {self.event_date}"
