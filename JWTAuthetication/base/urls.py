from django.urls import path,include
from .models import Student
from .serializers import StudentSerializer
from rest_framework.routers import DefaultRouter
from .views import StudentCRUD,CustomTokenObtainPairView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = DefaultRouter()
router.register('',StudentCRUD,basename='StudentCRUD')

urlpatterns = [
    path('',include(router.urls)),
    # path('get_token',TokenObtainPairView.as_view(),name='get_token'),
    path('get_token',CustomTokenObtainPairView.as_view(),name='get_token'),
    path('refresh',TokenRefreshView.as_view(),name='refresh'),
    path('verify',TokenVerifyView.as_view(),name='verify')
]