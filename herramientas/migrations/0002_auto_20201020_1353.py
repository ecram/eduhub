# Generated by Django 2.2.15 on 2020-10-20 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enlace',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='herramienta',
            old_name='Descripcion',
            new_name='descripcion',
        ),
    ]
