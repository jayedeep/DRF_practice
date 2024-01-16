from django.urls import path,include
from .views import StudentCrud
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',StudentCrud,basename='StudentCrud')

urlpatterns = [
    path('',include(router.urls))
]