from django.urls import path
from .views import StudentCRUDView
urlpatterns = [
    path('',StudentCRUDView.as_view(),name='student_list_create'),
    path('<int:id>', StudentCRUDView.as_view(), name='student_update_retrive_delete')

]