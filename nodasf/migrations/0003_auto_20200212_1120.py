# Generated by Django 3.0.2 on 2020-02-12 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0002_auto_20200122_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Author'),
        ),
    ]
