# Generated by Django 2.0.5 on 2018-09-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cartitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='number_of_product',
            field=models.IntegerField(),
        ),
    ]
