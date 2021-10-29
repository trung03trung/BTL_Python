# Generated by Django 3.2.7 on 2021-10-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211015_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='catec_id',
            field=models.IntegerField(choices=[(1, 'Áo khoác'), (2, 'Áo sơ mi'), (4, 'Quần jean'), (5, 'Áo thun'), (6, 'Áo nỉ/Áo hoodie'), (7, 'Quần dài/Quần âu'), (8, 'Quần short')]),
        ),
    ]