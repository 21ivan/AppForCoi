# Generated by Django 4.0.4 on 2022-06-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='direction',
        ),
        migrations.AddField(
            model_name='doctor',
            name='direction',
            field=models.ManyToManyField(to='doctors.direction'),
        ),
    ]
