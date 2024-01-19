from django.urls import path,include
from .views import ProductViewSet,ProductPhotoViewSet,ProductPhotoMultiFile
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product',ProductViewSet,basename='products')
router.register('product_photo',ProductPhotoViewSet,basename='productphoto')

urlpatterns = [
    path('',include(router.urls)),
    path('custom/products',ProductPhotoMultiFile.as_view(),name='custom_products')
]