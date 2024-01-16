from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from .customauthentication import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StudentCrud(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]