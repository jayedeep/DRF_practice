from django.urls import path
from .views import get_all_students,student_crud

urlpatterns = [
    path('',get_all_students,name = 'student_list'),
    path('student',student_crud,name = 'student_crud'),
    path('student/<int:id>',student_crud,name = 'student_crud')
]