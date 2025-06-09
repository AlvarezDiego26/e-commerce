from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, OrderViewSet, OrderItemViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
