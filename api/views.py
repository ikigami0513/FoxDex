from django.shortcuts import render
from django.views.generic import View
from app.models import *

class PokemonNumeroApiView(View):
    def get(self, request, numero):
        try:
            pokemon = Pokemon.objects.get(numero=numero)
        except Pokemon.DoesNotExist:
            return render(request, 'error404.json', {'error': f'pokemon {numero} did not found'}, content_type='application/json')
            
        return render(request, 'pokemon.json', {'pokemon': pokemon}, content_type='application/json')
    
class PokemonNameApiView(View):
    def get(self, request, name):
        try:
            pokemon = Pokemon.objects.get(name=name.capitalize())
        except Pokemon.DoesNotExist:
            return render(request, 'error404.json', {'error': f'pokemon {name} did not found'}, content_type='application/json')
        
        return render(request, 'pokemon.json', {'pokemon': pokemon}, content_type='application/json')