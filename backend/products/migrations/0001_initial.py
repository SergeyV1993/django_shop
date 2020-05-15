# Generated by Django 3.0.3 on 2020-03-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default=None, max_length=128, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='/fake', null=True, upload_to='product_image')),
                ('discount', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('update', models.DateTimeField(auto_now=True, db_index=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]