# Generated by Django 3.2.7 on 2021-10-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_userpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_amount',
            field=models.IntegerField(default=0),
        ),
    ]