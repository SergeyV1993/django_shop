from backend.account.models import Account
from backend.products.models import *
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name='Наименование статуса')
    is_active = models.BooleanField(default=True, verbose_name='Доступность')
    create = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name_plural = 'Статусы'
        verbose_name = 'Статус'

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, db_index=True, verbose_name='Пользователь')
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Личный кабинет')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1, verbose_name='Статус')
    customer_email = models.EmailField(blank=True, null=True, default=None, db_index=True, verbose_name='Почта пользователя')
    customer_name = models.CharField(max_length=30, db_index=True, verbose_name='Имя пользователя')
    customer_phone = models.CharField(max_length=20, blank=True, null=True, default=None, db_index=True, verbose_name='Телефон пользователя')
    comments = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сумма заказа')
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

    def __str__(self):
        return str(self.id)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_index=True, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Продукт')
    number_of_product = models.IntegerField(default=1, verbose_name='Количество продукта')
    price_one_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена за штуку')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая цена')  # price * number
    is_active = models.BooleanField(default=True, verbose_name='Доступность')
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name_plural = 'Продукты в заказе'
        verbose_name = 'Продукт в заказе'

    def __str__(self):
        return str(self.product.name)

    def save(self, *args, **kwargs):
        self.price_one_item = self.product.price
        self.total_price = 0
        self.total_price = self.number_of_product * self.price_one_item
        super().save(*args, **kwargs)
