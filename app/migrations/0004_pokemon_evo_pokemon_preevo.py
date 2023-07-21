# Generated by Django 4.2.1 on 2023-07-20 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_pokemon_type1_alter_pokemon_type2'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='evo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_evolution', to='app.pokemon'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='preevo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evolution', to='app.pokemon'),
        ),
    ]
