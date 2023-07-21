from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from .models import *

class NationalPokedexView(View):
    def get(self, request):
        pokedex = Pokemon.objects.all()
        return render(request, 'nationalPokedex.html', context={
            'pokedex': pokedex,
        })
    
class PokedexView(View):
    def get(self, request, version):
        try:
            game = Game.objects.get(name=version)
        except Game.DoesNotExist:
            return render(request, 'error404.html')
        
        return render(request, 'pokedex.html', context={
            'game': game
        })
    
class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'game.html', context={
            'games': games,
        })