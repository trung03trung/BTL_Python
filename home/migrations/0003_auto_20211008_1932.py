# Generated by Django 3.2.7 on 2021-10-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211008_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='product_image1',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
