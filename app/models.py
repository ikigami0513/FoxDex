from django.db import models
from django.contrib.auth.models import User
from .utils import format_pokedex_number

class Pokemon(models.Model):
    TYPE = (
        ('Acier', 'Acier'),
        ('Combat', 'Combat'),
        ('Dragon', 'Dragon'),
        ('Eau', 'Eau'),
        ('Électrique', 'Électrique'),
        ('Fée', 'Fée'),
        ('Feu', 'Feu'),
        ('Glace', 'Glace'),
        ('Insecte', 'Insecte'),
        ('Normal', 'Normal'),
        ('Plante', 'Plante'),
        ('Poison', 'Poison'),
        ('Psy', 'Psy'),
        ('Roche', 'Roche'),
        ('Sol', 'Sol'),
        ('Spectre', 'Spectre'),
        ('Ténèbres', 'Ténèbres'),
        ('Vol', 'Vol')
    )

    numero = models.IntegerField()
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='pokemon/')

    taille = models.FloatField(default=0)
    poids = models.FloatField(default=0)
    categorie = models.CharField(max_length=50, default="")

    type1 = models.CharField(max_length=15, choices=TYPE, default=TYPE[0])
    type2 = models.CharField(max_length=15, choices=TYPE, null=True)

    pv = models.IntegerField()
    attaque = models.IntegerField()
    defense = models.IntegerField()
    attaque_spe = models.IntegerField()
    defense_spe = models.IntegerField()
    vitesse = models.IntegerField()

    def __str__(self) -> str:
        return f"{format_pokedex_number(self.numero)} # {self.name}"
    
    def format_number(self):
        return format_pokedex_number(self.numero)
    
class Evolution(models.Model):
    class Meta:
        verbose_name = "Évolution"
        verbose_name_plural = "Évolutions"

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="evolution")
    evolution = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="pokemon")
    condition = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.pokemon.name} -> {self.condition} -> {self.evolution.name}"
    
class Game(models.Model):
    class Meta:
        verbose_name = "Jeu"
        verbose_name_plural = "Jeux"

    name = models.CharField(max_length=40)
    jaquette = models.ImageField(upload_to="jaquette/")

    def __str__(self) -> str:
        return f"Pokemon version {self.name}"

class PokemonInstance(models.Model):
    class Meta:
        verbose_name = "Instance Pokémon"
        verbose_name_plural = "Instances Pokémon"

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="instances")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="pokemons")

    numero = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.pokemon.name} de {self.game}"
    
class Extension(models.Model):
    class Meta:
        verbose_name = "Extension d'utilisateur"
        verbose_name_plural = "Extensions d'utilisateurs"

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    friends = models.ManyToManyField(User, related_name="friends")
    pokemons = models.ManyToManyField(PokemonInstance, related_name="users")

    def __str__(self) -> str:
        return self.user.username