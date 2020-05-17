from django.db import models
from django.conf import settings


class Account(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, db_index=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Личные кабинеты'
        verbose_name = 'Личный кабинет'

    def __str__(self):
        return str(self.id)
