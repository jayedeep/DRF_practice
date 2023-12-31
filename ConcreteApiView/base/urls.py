from django.urls import path
from .views import StudentCreateList,StudentRetriveUpdateDestroy

urlpatterns = [
    path('',StudentCreateList.as_view(),name = 'student_list_create'),
    path('<int:id>',StudentRetriveUpdateDestroy.as_view(),name = 'student_update_retrive_delete'),

  ]