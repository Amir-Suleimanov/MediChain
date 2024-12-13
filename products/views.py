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
        try:
                cargo = self.get_object()
        except Cargo.DoesNotExist:
            return Response({"error": "Cargo not found"}, status=status.HTTP_404_NOT_FOUND)

        if cargo.storage_cell:
            return Response(
                {"message": "Cargo already has a storage cell", "storage_cell": cargo.storage_cell.identifier},
                status=status.HTTP_200_OK,
            )

        available_cells = StorageCell.objects.filter(
            capacity__gte=F('current_load') + cargo.volume,
            current_load=0.0,
        ).order_by('capacity')

        if not available_cells.exists():
            return Response({"error": "No suitable storage cell found"}, status=status.HTTP_404_NOT_FOUND)

        selected_cell = available_cells.first()
        cargo.storage_cell = selected_cell
        cargo.save()

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


