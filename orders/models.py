from django.db import models


class OrderRequest(models.Model):
    cargo = models.ForeignKey('products.Cargo', on_delete=models.CASCADE, related_name='order_requests', verbose_name='Товар')  # Товар, который хотят отправить
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # Дата создания заявки
    is_completed = models.BooleanField(default=False, verbose_name='Выполнена ли заявка')  # Выполнена ли заявка

    def __str__(self):
        return f"OrderRequest for {self.cargo.name} - {'Completed' if self.is_completed else 'Pending'}"