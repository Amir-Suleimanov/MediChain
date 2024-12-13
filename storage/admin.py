# products/admin.py
from django.contrib import admin
from storage.models import StorageCell

@admin.register(StorageCell)
class StorageCellAdmin(admin.ModelAdmin):
    list_display = (
        'identifier', 
        'capacity', 
        'current_load', 
        'height', 
        'width'
    )  # Поля, отображаемые в списке
    list_filter = ('capacity',)  # Возможность фильтрации по объему
    search_fields = ('identifier',)  # Поиск по названию ячейки
    ordering = ('identifier',)  # Сортировка по названию ячейки

    # Настройка отображения связанных товаров
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('cargos')  # Оптимизация запросов

    def cargos_list(self, obj):
        return ", ".join([cargo.name for cargo in obj.cargos.all()])
    cargos_list.short_description = 'Товары в ячейке'
