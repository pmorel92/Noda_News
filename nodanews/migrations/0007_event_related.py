# Generated by Django 3.0.2 on 2020-01-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0006_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='related',
            field=models.ManyToManyField(blank=True, null=True, to='nodanews.Event'),
        ),
    ]
