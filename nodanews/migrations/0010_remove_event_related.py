# Generated by Django 3.0.2 on 2020-01-24 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0009_auto_20200124_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='related',
        ),
    ]
