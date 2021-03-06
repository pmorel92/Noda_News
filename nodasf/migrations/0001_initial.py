# Generated by Django 3.0.2 on 2020-01-17 17:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bureaucrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default='last', max_length=100)),
                ('first_name', models.CharField(default='first', max_length=100)),
                ('picture', models.ImageField(default=' ', upload_to='media/faces')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default=' ')),
                ('image', models.ImageField(blank=True, default='', upload_to='media/stock')),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('free', models.BooleanField(default=False)),
                ('cost', models.CharField(blank=True, default='', max_length=100)),
                ('homepage', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField()),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/stock')),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/stock')),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Media_Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('home_page', models.CharField(default='', max_length=200)),
                ('country', models.CharField(default='', max_length=100)),
                ('date_founded', models.DateField(default='1956-02-27')),
                ('logo', models.ImageField(upload_to='media/logos')),
                ('description', models.TextField()),
                ('ready', models.BooleanField(default=False)),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('picture', models.ImageField(default=' ', upload_to='media/stock')),
                ('homepage', models.CharField(default='', max_length=300)),
                ('description', models.TextField()),
                ('slug', models.SlugField(default=' ', max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Category')),
                ('issue', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Issue')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='first', max_length=100)),
                ('last_name', models.CharField(default='last', max_length=100)),
                ('picture', models.ImageField(default=' ', upload_to='media/faces')),
                ('homepage', models.CharField(default='', max_length=300)),
                ('description', models.TextField()),
                ('candidate', models.BooleanField(default=False)),
                ('slug', models.SlugField(default=' ', max_length=100)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodasf.District')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodasf.Level')),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodasf.Party')),
                ('upcoming', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodasf.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('homepage', models.CharField(default=' ', max_length=300)),
                ('description', models.TextField(default=' ')),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/stock')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Category')),
                ('issue', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Issue')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nodasf.Organization')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default=' ')),
                ('homepage', models.CharField(default=' ', max_length=300)),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/stock')),
                ('slug', models.SlugField(default=' ', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default=' ', max_length=150)),
                ('lead', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='', upload_to='media/stock')),
                ('credit', models.CharField(default='', max_length=200)),
                ('videoQ', models.BooleanField(default=False)),
                ('video', models.CharField(blank=True, default='', max_length=500)),
                ('slug', models.SlugField(default=' ', max_length=100)),
                ('bureaucrat', models.ManyToManyField(blank=True, to='nodasf.Bureaucrat')),
                ('issue', models.ManyToManyField(to='nodasf.Issue')),
                ('politician', models.ManyToManyField(blank=True, to='nodasf.Politician')),
                ('program', models.ManyToManyField(blank=True, to='nodasf.Program')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Report_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', max_length=300)),
                ('title', models.CharField(blank=True, default='', max_length=150)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/temp')),
                ('media', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Media_Org')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodasf.Story')),
            ],
            options={
                'ordering': ('-posted',),
            },
        ),
        migrations.CreateModel(
            name='Local_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=300)),
                ('headline', models.CharField(default='', max_length=150)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('imageQ', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/stock')),
                ('issue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Issue')),
            ],
            options={
                'ordering': ('-posted',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodasf.Genre'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Venue'),
        ),
        migrations.AddField(
            model_name='district',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Level'),
        ),
        migrations.AddField(
            model_name='bureaucrat',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodasf.Organization'),
        ),
        migrations.AddField(
            model_name='bureaucrat',
            name='program',
            field=models.ManyToManyField(blank=True, to='nodasf.Program'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='', max_length=200)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('slug', models.SlugField(default=' ', max_length=200)),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Story')),
            ],
            options={
                'ordering': ('-date_posted',),
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('picture', models.ImageField(default=' ', upload_to='media/stock')),
                ('homepage', models.CharField(default='', max_length=300)),
                ('description', models.TextField()),
                ('slug', models.SlugField(default=' ', max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Category')),
                ('issue', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.Issue')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
