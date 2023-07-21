from django.urls import path
from rest_framework.authtoken import views as rest_views
from .views import *

urlpatterns = [
    path('token/', rest_views.obtain_auth_token, name='token'),
    path('pokemon/<int:numero>/', PokemonNumeroApiView.as_view(), name='api_pokemon_numero'),
    path('pokemon/<str:name>/', PokemonNameApiView.as_view(), name='api_pokemon_name'),
]