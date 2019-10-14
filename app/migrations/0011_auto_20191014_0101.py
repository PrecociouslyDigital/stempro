# Generated by Django 2.2.1 on 2019-10-14 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_signupevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='event',
            name='when',
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
