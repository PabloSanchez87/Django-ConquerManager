# Generated by Django 5.0.6 on 2024-06-30 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
            ],
            options={
                'verbose_name': 'Familia',
                'verbose_name_plural': 'Familias',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('age', models.IntegerField(default=18, help_text='Introduce tu edad en formato número.', verbose_name='Edad')),
                ('dni', models.CharField(max_length=9, unique=True, verbose_name='DNI')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.family')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['age'],
            },
        ),
    ]
