from django.urls import path
from .views import get_student,all_student,create_student


urlpatterns = [
    path('student',all_student,name = 'all_student'),
    path('student/<int:id>',get_student,name = 'get_student'),
    path('student/create',create_student,name = 'create_student'),

]