from django import forms
from .models import Game

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'category', 'quantity', 'available']
