# Generated by Django 3.0.8 on 2020-07-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200718_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='pic',
            field=models.ImageField(default='../Blog/blog/static/blog/pic_folder/None/no-img.jpg', upload_to='../Blog/blog/static/blog/pic_folder/'),
        ),
    ]
