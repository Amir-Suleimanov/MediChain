from rest_framework import generics
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, ExpressionWrapper, FloatField

from products.models import Cargo
from products.serializers import CargoSerializer
from storage.models import StorageCell


class CargoRetrieveViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    @action(detail=True, methods=['get'], url_path='get-storage-cell')
    def get_storage_cell(self, request, pk=None):
        # Получаем груз по id
        try:
            cargo = self.get_object()
        except Cargo.DoesNotExist:
            return Response({"error": "Cargo not found"}, status=status.HTTP_404_NOT_FOUND)

        # Проверка: если у груза уже назначена ячейка, вернуть её
        if cargo.storage_cell:
            return Response(
                {"message": "Cargo already has a storage cell", "storage_cell": cargo.storage_cell.identifier},
                status=status.HTTP_200_OK,
            )

        # Вычисление оставшегося свободного объема для каждой ячейки
        available_cells = StorageCell.objects.annotate(
            free_space=ExpressionWrapper(
                F('capacity') - F('current_load'), output_field=FloatField()
            )
        ).filter(
            free_space__gte=cargo.volume  # Ячейки, в которые поместится груз
        ).order_by('free_space')  # Минимально возможный оставшийся объем

        # Проверяем, есть ли подходящая ячейка
        if not available_cells.exists():
            return Response({"error": "No suitable storage cell found"}, status=status.HTTP_404_NOT_FOUND)

        # Назначаем первую подходящую ячейку
        selected_cell = available_cells.first()
        cargo.storage_cell = selected_cell
        cargo.save()  # Это вызовет сигнал для обновления current_load

        # Возвращаем информацию о выбранной ячейке
        return Response(
            {
                "message": "Storage cell assigned successfully",
                "storage_cell": {
                    "identifier": selected_cell.identifier,
                    "capacity": selected_cell.capacity,
                    "current_load": selected_cell.current_load,
                    "free_space": selected_cell.capacity - selected_cell.current_load,
                },
            },
            status=status.HTTP_200_OK,
        )
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    @action(detail=True, methods=['get'], url_path='get-storage-cell')
    def get_storage_cell(self, request, pk=None):
        # Получаем груз по id
        try:
            cargo = self.get_object()
        except Cargo.DoesNotExist:
            return Response({"error": "Cargo not found"}, status=status.HTTP_404_NOT_FOUND)

        # Проверка: если у груза уже назначена ячейка, вернуть её
        if cargo.storage_cell:
            return Response(
                {"message": "Cargo already has a storage cell", "storage_cell": cargo.storage_cell.identifier},
                status=status.HTTP_200_OK,
            )

        # Фильтруем доступные ячейки
        available_cells = StorageCell.objects.filter(
            capacity__gte=F('current_load') + cargo.volume,  # Достаточно места
            current_load=0.0,  # Ячейка свободна
        ).order_by('capacity')  # Наименьший подходящий объем

        # Проверяем, есть ли подходящая ячейка
        if not available_cells.exists():
            return Response({"error": "No suitable storage cell found"}, status=status.HTTP_404_NOT_FOUND)

        # Назначаем первую подходящую ячейку
        selected_cell = available_cells.first()
        cargo.storage_cell = selected_cell
        cargo.save()

        # Возвращаем информацию о выбранной ячейке
        return Response(
            {
                "message": "Storage cell assigned successfully",
                "storage_cell": {
                    "identifier": selected_cell.identifier,
                    "capacity": selected_cell.capacity,
                    "current_load": selected_cell.current_load,
                },
            },
            status=status.HTTP_200_OK,
        )


class CargoCreateAPIView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


