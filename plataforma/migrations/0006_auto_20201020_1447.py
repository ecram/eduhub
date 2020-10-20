# Generated by Django 2.2.15 on 2020-10-20 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_auto_20201020_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='observaciones_sugerencias',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(1500)], verbose_name='Describa las observaciones y sugerencias'),
        ),
    ]
