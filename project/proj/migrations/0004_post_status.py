# Generated by Django 4.0.4 on 2022-05-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0003_category_post_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
