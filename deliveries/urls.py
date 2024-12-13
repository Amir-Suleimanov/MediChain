# cargo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from deliveries.views import DeliveryViewSet

router = DefaultRouter()
router.register(r'deliveries', DeliveryViewSet, basename='delivery')

urlpatterns = [
    path('', include(router.urls)),
]
