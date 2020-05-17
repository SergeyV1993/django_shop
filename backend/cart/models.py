from backend.products.models import *
from django.contrib.auth.models import UserManager


class Cart(models.Model):
    cart_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сумма')
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True, verbose_name='Дата последнего обновления')

    objects = UserManager()

    class Meta:
        verbose_name_plural = 'Корзина'
        verbose_name = 'Корзина'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.cart_item_price = 0
        super().save(*args, **kwargs)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    number_of_product = models.IntegerField(default=0, verbose_name='Количество товара')
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая сумма за товар')

    class Meta:
        verbose_name_plural = 'Товары в корзине'
        verbose_name = 'Товар в корзине'

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        price_one_item = self.product.price
        self.total_item_price = 0
        self.total_item_price = self.number_of_product * price_one_item
        super().save(*args, **kwargs)
