# Generated by Django 5.0.3 on 2024-04-13 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_episodios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Episodios',
            new_name='Episodio',
        ),
    ]
