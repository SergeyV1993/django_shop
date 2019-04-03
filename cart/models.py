from products.models import *
from django.contrib.auth.models import UserManager


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    number_of_product = models.IntegerField(default=0, verbose_name='Количество товара')
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая сумма за товар')

    class Meta:
        verbose_name_plural = 'Товары в корзине'
        verbose_name = 'Товар в корзине'

    def __str__(self):
        try:
            return self.product.name
        except Exception as error:
            print(error)

    def save(self, *args, **kwargs):
        price_one_item = self.product.price
        self.total_item_price = 0
        self.total_item_price = self.number_of_product * price_one_item
        super().save(*args, **kwargs)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True, db_index=True)
    cart_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = UserManager()

    def __str__(self):
        try:
            return str(self.id)
        except Exception as error:
            print(error)

    def save(self, *args, **kwargs):
        self.cart_item_price = 0
        super().save(*args, **kwargs)