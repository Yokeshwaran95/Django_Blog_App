# Generated by Django 3.0.8 on 2020-08-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[('Automotive', 'Automotive'), ('Gadgets', 'Gadgets'), ('Science', 'Science'), ('Technology', 'Technology')], default='Automotive'),
        ),
    ]
