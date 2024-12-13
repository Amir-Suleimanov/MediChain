from rest_framework.routers import DefaultRouter
from django.urls import path

from products.views import CargoCreateAPIView, CargoRetrieveViewSet


router = DefaultRouter()

router.register('', CargoRetrieveViewSet, basename='cargo')
    

urlpatterns = [
    path('create/', CargoCreateAPIView.as_view(), name='create-cargo')
] + router.urls