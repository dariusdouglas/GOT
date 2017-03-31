# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('times_killed', models.IntegerField(default=0)),
                ('manner_of_death', models.CharField(blank=True, max_length=255, null=True)),
                ('times_won_throne', models.IntegerField(default=0)),
                ('times_survived', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='/images/')),
                ('birthplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birthplace', to='location.Location')),
                ('location_of_death', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_of_death', to='location.Location')),
                ('murderer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
    ]
