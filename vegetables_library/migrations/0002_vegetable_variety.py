# Generated by Django 2.0.1 on 2018-03-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetables_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vegetable',
            name='variety',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
