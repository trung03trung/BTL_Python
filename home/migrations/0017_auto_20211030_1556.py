# Generated by Django 3.2.7 on 2021-10-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20211029_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(upload_to='home/static/media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(null=True, upload_to='home/static/media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(null=True, upload_to='home/static/media'),
        ),
    ]