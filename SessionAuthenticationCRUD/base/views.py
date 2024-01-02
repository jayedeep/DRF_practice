from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from .custom_permission import CustomPermission

class StudentCrud(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]

