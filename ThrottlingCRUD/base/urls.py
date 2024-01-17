from django.urls import path,include
from .views import StudentCRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',StudentCRUD,basename='student_crud')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls'))  # this will add user login functionality

]