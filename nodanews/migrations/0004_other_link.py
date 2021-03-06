# Generated by Django 3.0.2 on 2020-01-17 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0003_blog_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', max_length=300)),
                ('title', models.CharField(blank=True, default='', max_length=150)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/temp')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Media_Org')),
            ],
            options={
                'ordering': ('-posted',),
            },
        ),
    ]
