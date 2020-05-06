# Generated by Django 3.0.2 on 2020-05-05 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0015_auto_20200505_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RenameField(
            model_name='event',
            old_name='credit',
            new_name='credit1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='event',
            name='body2',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='event',
            name='column',
            field=models.CharField(choices=[('L', 'Left'), ('M', 'Middle'), ('R', 'Right')], default='L', max_length=1),
        ),
        migrations.AddField(
            model_name='event',
            name='credit2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='image2',
            field=models.ImageField(default='', upload_to='media/stock'),
        ),
        migrations.AddField(
            model_name='other_link',
            name='conservative',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='other_link',
            name='liberal',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='other_link',
            name='major',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='body',
            field=models.TextField(default=' '),
        ),
        migrations.CreateModel(
            name='Front_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featureQ', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('feature_headline', models.CharField(blank=True, default=' ', max_length=150)),
                ('feature_url', models.CharField(blank=True, default='', max_length=300)),
                ('feature_pic', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('feature_pic_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('right_pic_1', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('right_pic_1_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('right_pic_2', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('right_pic_2_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('middle_pic_1', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('middle_pic_1_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('middle_pic_2', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('middle_pic_2_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('left_pic_1', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('left_pic_1_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('left_pic_2', models.ImageField(blank=True, default=' ', upload_to='media/stock')),
                ('left_pic_2_credit', models.CharField(blank=True, default=' ', max_length=150)),
                ('slug', models.SlugField(default='date', max_length=100)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Variation')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='front_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Front_Page'),
        ),
        migrations.AddField(
            model_name='other_link',
            name='front_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Front_Page'),
        ),
    ]