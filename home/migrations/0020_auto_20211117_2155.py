# Generated by Django 3.2.7 on 2021-11-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20211110_1652'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPassword',
        ),
        migrations.AlterField(
            model_name='category_chile',
            name='catep_id',
            field=models.IntegerField(choices=[(1, 'Áo'), (2, 'Quần'), (3, 'Giày'), (5, 'Đồ bộ')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='catep_id',
            field=models.IntegerField(choices=[(1, 'Áo'), (2, 'Quần'), (3, 'Giày'), (5, 'Đồ bộ')]),
        ),
    ]
