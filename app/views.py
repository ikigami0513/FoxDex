from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator
from .models import *
from .forms import *

class NationalPokedexView(View):
    def get(self, request):
        pokedex = Pokemon.objects.all()
        return render(request, 'pokemon/nationalPokedex.html', context={
            'pokedex': pokedex,
        })
    
class PokedexView(View):
    def get(self, request, version):
        try:
            game = Game.objects.get(name=version)
        except Game.DoesNotExist:
            return render(request, 'error/error404.html')
        
        return render(request, 'pokemon/pokedex.html', context={
            'game': game
        })
    
class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'pokemon/game.html', context={
            'games': games,
        })
    
class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    
class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        
        return render(request, 'user/login.html')
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'user/login.html', {
                'error_message': 'Invalid login',
            })
        
class UserRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        
        return render(request, 'user/register.html')
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")

        return render(request, "user/register.html")

class SettingsView(View):
    def get(self, request):
        return render(request, 'user/settings.html')