# Generated by Django 5.0.6 on 2024-06-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_remove_person_id_person_dni_alter_person_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='dni',
            field=models.CharField(max_length=9),
        ),
    ]