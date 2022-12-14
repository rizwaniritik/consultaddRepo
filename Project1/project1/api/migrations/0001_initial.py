# Generated by Django 4.1.1 on 2022-09-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=80)),
                ('caption', models.CharField(max_length=80)),
                ('version', models.CharField(max_length=80)),
                ('date', models.DateField(max_length=80)),
            ],
        ),
    ]
