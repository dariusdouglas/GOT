# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20170331_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/images/'),
        ),
    ]