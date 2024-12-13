from django.db import models


class Supplier(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')  # ФИО
    passport = models.CharField(max_length=15, unique=True, verbose_name='Паспортные данные')  # Паспортные данные
    experience = models.PositiveIntegerField(verbose_name='Стаж в годах')  # Стаж в годах
    delivered_goods_count = models.PositiveIntegerField(default=0, verbose_name='Кол-во доставленных товаров')  # Кол-во доставленных товаров
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Баланс')  # Баланс
    photo = models.ImageField(upload_to='suppliers/photos/', verbose_name='Фото')  # Фото

    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.full_name
