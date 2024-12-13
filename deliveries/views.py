# cargo/views.py
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from deliveries.models import Delivery
from suppliers.models import Supplier
from deliveries.serializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    # Ручка для добавления грузчика в поставку
    @action(detail=True, methods=['put'], url_path='add-supplier')
    def add_supplier(self, request, pk=None):
        # Получаем поставку по id (pk)
        delivery = self.get_object()

        # Получаем список всех поставщиков
        suppliers = Supplier.objects.all()

        # Получаем грузчиков, которые уже добавлены в поставку
        assigned_suppliers = delivery.workers_assigned.all()

        # Фильтруем поставщиков, которые еще не назначены на эту поставку
        unassigned_suppliers = suppliers.exclude(id__in=assigned_suppliers.values_list('id', flat=True))

        # Добавляем нового грузчика, если передан ID поставщика
        supplier_id = request.data.get('supplier_id')
        if supplier_id:
            try:
                supplier = Supplier.objects.get(id=supplier_id)
                if supplier not in assigned_suppliers:
                    delivery.workers_assigned.add(supplier)
                    delivery.save()
                    return Response(DeliverySerializer(delivery).data)
                else:
                    return Response({"detail": "Грузчик уже назначен на эту поставку."}, status=status.HTTP_400_BAD_REQUEST)
            except Supplier.DoesNotExist:
                return Response({"detail": "Поставщик не найден."}, status=status.HTTP_404_NOT_FOUND)

        # Возвращаем список грузчиков, которые не назначены на данную поставку
        return Response([{'id': supplier.id, 'full_name': supplier.full_name} for supplier in unassigned_suppliers], status=status.HTTP_200_OK)
