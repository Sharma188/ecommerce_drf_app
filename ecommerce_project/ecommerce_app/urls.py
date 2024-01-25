from django.urls import path, include
from ecommerce_project.ecommerce_app import views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees', views.UserViewSet)
router.register('employees', views.ProductViewSet)
router.register('employees', views.CategoryViewSet)
router.register('employees', views.CartViewSet)
router.register('employees', views.OrderViewSet)
router.register('employees', views.FileUploadView)

urlpatterns = [
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
