from django.db import models


class StorageCell(models.Model):
    identifier = models.CharField(max_length=10, unique=True, verbose_name='Название ячейки')  # Название ячейки (буква + цифра)
    height = models.FloatField(verbose_name='Высота')  # Высота
    width = models.FloatField(verbose_name='Ширина')  # Ширина
    length = models.FloatField(default=1.0, verbose_name='Длина')  # Длина (фиксированная)
    capacity = models.FloatField(verbose_name='Максимальная вместимость в куб. метрах')  # Максимальная вместимость в куб. метрах
    current_load = models.FloatField(default=0.0, verbose_name='Текущая загрузка')  # Текущая загрузка

    def __str__(self):
        return self.identifier