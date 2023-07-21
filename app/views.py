from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator
from .models import *
from .forms import *

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
    
class AddPokemon(View):
    def get(self, request):
        form = PokemonForm()
        return render(request, 'addPokemon.html', context={
            'form': form
        })
    
    def post(self, request):
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("add_pokemon")

        return render(request, 'addPokemon.html', context={
            'form': form,
        })
    
class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    
class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {
                'error_message': 'Invalid login',
            })