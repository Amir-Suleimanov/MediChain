from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'experience', 'balance', 'delivered_goods_count')
    list_filter = ('is_staff',)
    search_fields = ('full_name',)
