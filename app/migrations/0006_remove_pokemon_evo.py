# Generated by Django 4.2.1 on 2023-07-20 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_pokemon_preevo_alter_pokemon_evo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evo',
        ),
    ]