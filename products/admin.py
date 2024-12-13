from django.contrib import admin
from products.models import Cargo

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'volume', 'delivery_date', 'shelf_life',)
    list_filter = ('delivery_date', 'shelf_life')
    search_fields = ('name',)


