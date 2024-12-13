# cargo/serializers.py
from rest_framework import serializers
from deliveries.models import Delivery
from suppliers.models import Supplier


class DeliverySerializer(serializers.ModelSerializer):
    workers_assigned = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), many=True)

    class Meta:
        model = Delivery
        fields = ['id', 'cargo_count', 'workers_assigned', 'delivery_date', 'is_unloaded']
