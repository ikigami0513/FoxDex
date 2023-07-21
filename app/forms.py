from django import forms 
from .models import Pokemon
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            'numero', 
            'name',
            'image',
            'taille',
            'poids',
            'categorie',
            'type1',
            'type2',
            'pv',
            'attaque',
            'defense',
            'attaque_spe',
            'defense_spe',
            'vitesse',
        ]

    def __init__(self, *args, **kwargs):
        super(PokemonForm, self).__init__(*args, **kwargs)
        self.fields['type2'].empty_value = None
        self.fields['type2'].required = False

    def clean_type2(self):
        type2 = self.cleaned_data['type2']
        return type2 if type2 != '' else None
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')