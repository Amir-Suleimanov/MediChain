from django.db import models

from suppliers.models import Supplier


class Delivery(models.Model):
    cargo_count = models.PositiveIntegerField(verbose_name='Кол-во поставленных товаров')  # Кол-во поставленных товаров
    workers_assigned = models.ManyToManyField(
        Supplier,
        related_name="deliveries",
        verbose_name="Назначенные грузчики"
    )
    delivery_date = models.DateField(verbose_name='Дата поставки')  # Дата поставки
    is_unloaded = models.BooleanField(default=False, verbose_name='Разгружен ли')  # Разгружен ли

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"
    
    def __str__(self):
        return f"Поставка от {self.delivery_date}, разгружен: {'Да' if self.is_unloaded else 'Нет'}"