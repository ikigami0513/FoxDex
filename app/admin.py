from django import forms
from django.contrib import admin
from .models import *
from .forms import *

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    form = PokemonForm
    fieldsets = (
        ('Informations', {
            'fields': ('numero', 'name', 'image', 'type1', 'type2')
        }),
        ('Data', {
            'fields': ('taille', 'poids', 'categorie')
        }),
        ('Stats', {
            'fields': ('pv', 'attaque', 'defense', 'attaque_spe', 'defense_spe', 'vitesse')
        })
    )

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