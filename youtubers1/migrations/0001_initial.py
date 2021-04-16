# Generated by Django 3.1.7 on 2021-04-05 02:42

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%Y/%m/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255)),
                ('camera_type', models.CharField(choices=[('sony', 'sony'), ('Mi', 'Mi'), ('Panasonic', 'Panasonic'), ('Canon', 'Canon'), ('Nikon', 'Nikon'), ('fuji', 'fuji'), ('samsung', 'samsung')], max_length=255)),
                ('subs_count', models.IntegerField()),
                ('cateogry', models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('cooking', 'cooking')], max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
