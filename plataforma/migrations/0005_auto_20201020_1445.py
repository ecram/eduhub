# Generated by Django 2.2.15 on 2020-10-20 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_auto_20201020_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='descripcion',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción del área'),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='descripcion',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Descripción del Nivel Académico'),
        ),
    ]
