from django.urls import path,include
from .views import StudentCRUDView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudentCRUDView, basename='student_crud')

urlpatterns = [
    path('',include(router.urls))
]