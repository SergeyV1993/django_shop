from products.models import *
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return self.name
        except Exception as error:
            print(error)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, db_index=True)
    customer_email = models.EmailField(blank=True, null=True, default=None, db_index=True)
    customer_name = models.CharField(max_length=30, db_index=True)
    customer_phone = models.CharField(max_length=20, blank=True, null=True, default=None, db_index=True)
    comments = models.TextField(blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True)

    def __str__(self):
        try:
            return self.customer_name
        except Exception as error:
            print(error)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    number_of_product = models.IntegerField(default=1)
    price_one_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price * number
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True)

    def __str__(self):
        try:
            return "Продукт %s" % self.product.name
        except Exception as error:
            print(error)

    def save(self, *args, **kwargs):
        self.price_one_item = self.product.price
        self.total_price = 0
        self.total_price = self.number_of_product * self.price_one_item
        super().save(*args, **kwargs)

