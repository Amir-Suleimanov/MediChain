from django.contrib import admin
from deliveries.models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo_count', 'delivery_date', 'is_unloaded')
    list_filter = ('delivery_date', 'is_unloaded')
    search_fields = ('id',)
