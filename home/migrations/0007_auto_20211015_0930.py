# Generated by Django 3.2.7 on 2021-10-15 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211014_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_chile',
            name='catec_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pro_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='catec_id',
            field=models.IntegerField(choices=[(1, 'Áo khoác'), (2, 'Áo sơ mi'), (4, 'Quần jean'), (5, 'Áo thun'), (6, 'Áo nỉ/Áo hoodie'), (7, 'Quần dài/Quần âu')]),
        ),
    ]
