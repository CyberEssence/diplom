# Generated by Django 4.0.4 on 2022-05-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0012_remove_video_new_field_video_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default='post', unique=True),
        ),
    ]
