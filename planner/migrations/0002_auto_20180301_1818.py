# Generated by Django 2.0.1 on 2018-03-01 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturaloperation',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Temps nécessaire par m²'),
        ),
    ]