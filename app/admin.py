from django import forms
from django.contrib import admin
from .models import *

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Evolution)
class EvolutionAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(PokemonInstance)
class PokemonInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    pass