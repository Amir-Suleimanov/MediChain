from django.db import models


class Cargo(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')  # Название
    volume = models.FloatField(verbose_name='Объем в куб. метрах')  # Объем в куб. метрах
    shelf_life = models.DateField(verbose_name='Срок хранения')  # Срок хранения
    description = models.TextField(blank=True, verbose_name='Описание')  # Описание
    delivery_date = models.DateField(auto_now_add=True, verbose_name='Дата поставки')  # Дата поставки
    pick_up_date = models.DateField(null=True, blank=True, verbose_name='Дата, когда товар забрали')  # Дата, когда товар забрали
    storage_cell = models.ForeignKey('storage.StorageCell', on_delete=models.SET_NULL, null=True, blank=True, related_name='cargos', verbose_name='Ячейка хранения')  # Ячейка хранения


    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
    
    
    def __str__(self):
        return self.name