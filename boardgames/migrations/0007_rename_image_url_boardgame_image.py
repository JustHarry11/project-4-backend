# Generated by Django 5.2.2 on 2025-06-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0006_alter_boardgame_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardgame',
            old_name='image_url',
            new_name='image',
        ),
    ]
