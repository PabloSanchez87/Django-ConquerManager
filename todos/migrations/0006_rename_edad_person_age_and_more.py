# Generated by Django 5.0.6 on 2024-06-21 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_alter_person_apellido_alter_person_dni_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='edad',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='nombre',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='apellido',
            new_name='last_name',
        ),
    ]
