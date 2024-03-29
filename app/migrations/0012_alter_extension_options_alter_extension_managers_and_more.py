# Generated by Django 4.2.1 on 2023-07-21 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_extension'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extension',
            options={},
        ),
        migrations.AlterModelManagers(
            name='extension',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='extension',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='email',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='password',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='username',
        ),
        migrations.AddField(
            model_name='extension',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
