# Generated by Django 3.0.7 on 2020-12-19 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empdetails',
            name='alt_mob_no',
        ),
    ]
