from django.contrib import admin
from suppliers.models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'passport', 'experience', 'delivered_goods_count', 'balance')
    search_fields = ('full_name', 'passport')
