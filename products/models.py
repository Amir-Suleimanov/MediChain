from django.db import models


class Cargo(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')  # Название
    volume = models.FloatField(verbose_name='Объем в куб. метрах')  # Объем в куб. метрах
    shelf_life = models.DateField(verbose_name='Срок хранения')  # Срок хранения
    description = models.TextField(blank=True, verbose_name='Описание')  # Описание
    delivery_date = models.DateField(verbose_name='Дата поставки')  # Дата поставки
    pick_up_date = models.DateField(null=True, blank=True, verbose_name='Дата, когда товар забрали')  # Дата, когда товар забрали
    storage_cell = models.ForeignKey('storage.StorageCell', on_delete=models.SET_NULL, null=True, related_name='cargos', verbose_name='Ячейка хранения')  # Ячейка хранения
    qr_code = models.CharField(max_length=255, blank=True, null=True, verbose_name='QR-код')  # QR-код как текстовое поле

    def __str__(self):
        return self.name