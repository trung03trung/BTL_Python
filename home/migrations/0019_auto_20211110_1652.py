# Generated by Django 3.2.7 on 2021-11-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211030_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(default='M', max_length=4),
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(default='M', max_length=4),
        ),
    ]
