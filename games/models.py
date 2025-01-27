import random
from django.db import models
import string

def generate_unique_code():
    """Genera un código único de 5 caracteres."""
    length = 5
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not Game.objects.filter(code=code).exists():  # Asegúrate de que el código no exista
            break
    return code


def save(self, *args, **kwargs):
    # Si no se ha asignado un código, genera uno nuevo
    if not self.code:
        self.code = self.generate_unique_code()
    super(Game, self).save(*args, **kwargs)


def __str__(self):
    return f"{self.name} - {self.code}"


class Meta:
    verbose_name = "Juego"
    verbose_name_plural = "Juegos"

class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Juego")
    category = models.CharField(max_length=50, default="General", verbose_name="Categoría")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    code = models.CharField(max_length=5, unique=True, default=generate_unique_code)
    available = models.BooleanField(default=True, verbose_name="Disponible")




class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.game.name} - {self.event_date}"
