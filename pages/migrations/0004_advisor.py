# Generated by Django 3.2.4 on 2021-06-15 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_expert_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255)),
                ('linkedin', models.URLField(max_length=100)),
                ('headshot', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('company1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('company2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
