# Generated by Django 4.2.7 on 2023-11-23 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='phrases',
            field=models.ManyToManyField(blank=True, to='api.phrase'),
        ),
    ]
