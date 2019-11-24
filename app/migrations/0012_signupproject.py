# Generated by Django 2.2.1 on 2019-10-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20191014_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('school_name', models.CharField(max_length=200)),
                ('grade', models.IntegerField(default=1)),
                ('first_choice', models.CharField(max_length=200, unique=True)),
                ('second_choice', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]