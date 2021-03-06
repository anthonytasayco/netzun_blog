# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField(default=0, editable=False, null=True, verbose_name='Creado por')),
                ('modified_by', models.IntegerField(default=0, editable=False, null=True, verbose_name='Modificado por')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=180, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='pulication')),
                ('featured', models.BooleanField(default=False, verbose_name='Destacado')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]
