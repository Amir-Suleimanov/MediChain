from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('suppliers/', include('suppliers.urls')),
    path('cargo/', include('products.urls')),
    # path('storage/', include('storage.urls')),
    path('deliveries/', include('deliveries.urls')),
    # path('orders/', include('orders.urls')),
]