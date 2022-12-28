# Generated by Django 4.1.4 on 2022-12-26 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='refrees',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('link', models.TextField(null=True, validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]
