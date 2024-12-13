from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Cargo

@receiver(post_save, sender=Cargo)
def update_storage_cell_load(sender, instance, **kwargs):
    """
    Обновляет заполненность ячейки, когда товар назначается на ячейку.
    """
    if instance.storage_cell:
        # Рассчитать текущую загрузку
        cell = instance.storage_cell
        cell.current_load += instance.volume
        cell.save()
