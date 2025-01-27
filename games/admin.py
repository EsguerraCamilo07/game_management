from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'code', 'available')
    search_fields = ('name', 'code')
