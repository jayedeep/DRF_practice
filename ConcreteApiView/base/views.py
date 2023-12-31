from django.shortcuts import render
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,
                                     UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentCreateList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# class StudentRetrive(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class StudentRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'