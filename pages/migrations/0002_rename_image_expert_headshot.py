# Generated by Django 3.2.4 on 2021-06-07 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expert',
            old_name='image',
            new_name='headshot',
        ),
    ]
