from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None, db_index=True, verbose_name='Наименование категории')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name
