from django.urls import path
from .views import StudentListCreate,StudentUpdateRetriveDelete

urlpatterns = [
    path('',StudentListCreate.as_view(),name = 'student_list_create'),
    path('<int:id>',StudentUpdateRetriveDelete.as_view(),name = 'student_update_retrive_delete'),

  ]