from django.urls import path, include
from ecommerce_project.ecommerce_app import views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('cart', views.CartViewSet)
router.register('orders', views.OrderViewSet)
router.register('files', views.FileUploadView)

urlpatterns = [
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
