# Generated by Django 4.2.1 on 2023-07-21 21:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_alter_extension_options_alter_extension_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='friends',
            field=models.ManyToManyField(related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
