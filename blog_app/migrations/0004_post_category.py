# Generated by Django 3.0.8 on 2020-07-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20200730_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'Automotive'), (1, 'Gadgets'), (2, 'Science'), (3, 'Technology')], default=0),
        ),
    ]
