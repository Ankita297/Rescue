# Generated by Django 3.0.6 on 2021-03-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_login_slideshowitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowitem',
            name='image',
            field=models.ImageField(upload_to='main_app/static/Images/slideshow'),
        ),
    ]
