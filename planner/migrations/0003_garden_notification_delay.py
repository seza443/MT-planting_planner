# Generated by Django 2.0.1 on 2018-03-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20180301_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='notification_delay',
            field=models.IntegerField(default=5),
        ),
    ]
