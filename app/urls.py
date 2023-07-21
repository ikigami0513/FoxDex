from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', NationalPokedexView.as_view(), name="national_pokedex"),
    path('pokedex/<str:version>', PokedexView.as_view(), name="pokedex"),
    path('games/', GameView.as_view(), name="games")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)