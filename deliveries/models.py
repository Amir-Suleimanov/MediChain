from django.db import models


class Delivery(models.Model):
    cargo_count = models.PositiveIntegerField(verbose_name='Кол-во поставленных товаров')  # Кол-во поставленных товаров
    workers_assigned = models.TextField(verbose_name='Список грузчиков, можно хранить в виде строки')  # Список грузчиков, можно хранить в виде строки
    delivery_date = models.DateField(verbose_name='Дата поставки')  # Дата поставки
    is_unloaded = models.BooleanField(default=False, verbose_name='Разгружен ли')  # Разгружен ли

    def __str__(self):
        return f"Delivery {self.id} - {self.cargo_count} items"