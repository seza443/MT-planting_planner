# Generated by Django 2.0.1 on 2018-02-27 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_auto_20180227_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alerts',
            old_name='executer',
            new_name='executor',
        ),
    ]
