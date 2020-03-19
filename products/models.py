from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='product_image', default='')
    discount = models.IntegerField(default=0)
    type = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True)

    def __str__(self):
        try:
            return "Продукт %s" % self.name
        except Exception as error:
            print(error)
