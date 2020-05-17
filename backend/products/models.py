from django.db import models
from backend.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None, db_index=True, verbose_name='Наименование продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='product_image', default='')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    type = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, db_index=True, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Доступность товара')
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    def __str__(self):
        return str(self.name)

