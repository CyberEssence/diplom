# Generated by Django 4.0.4 on 2022-05-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0009_alter_video_new_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
