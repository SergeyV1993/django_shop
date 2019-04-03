# Generated by Django 2.0.5 on 2019-04-03 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20190403_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='number_of_product',
            field=models.IntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total_item_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая сумма за товар'),
        ),
    ]
