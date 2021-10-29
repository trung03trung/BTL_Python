# Generated by Django 3.2.7 on 2021-10-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211022_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_chile',
            name='catep_id',
            field=models.IntegerField(choices=[(1, 'Áo'), (2, 'Quần'), (3, 'Gìay'), (5, 'Đồ bộ')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='catec_id',
            field=models.IntegerField(choices=[(1, 'Áo khoác'), (2, 'Áo sơ mi'), (4, 'Quần jean'), (5, 'Áo thun'), (6, 'Áo nỉ/Áo hoodie'), (7, 'Quần dài/Quần âu'), (8, 'Quần short'), (9, 'Giày thể thao/Sneakers'), (10, 'Giày tây lười'), (11, 'Giày lười'), (12, 'Đồ ngủ'), (13, 'Đồ thể thao'), (14, 'Quần jogger')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='catep_id',
            field=models.IntegerField(choices=[(1, 'Áo'), (2, 'Quần'), (3, 'Gìay'), (5, 'Đồ bộ')]),
        ),
       
    ]