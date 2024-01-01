from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

class StudentCrud(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication] # check settings.py there is globally defined
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            # Override permissions for the 'list' method (GET request)
            return [AllowAny()]
        elif self.action == 'create':
            # Override permissions for the 'create' method (POST request)
            return [IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update':
            # Override permissions for the 'update' and 'partial_update' methods (PUT and PATCH requests)
            return [IsAdminUser()]
        elif self.action == 'destroy':
            # Override permissions for the 'destroy' method (DELETE request)
            return [IsAdminUser()]

        # Use the default permissions for other methods
        return super(StudentCrud, self).get_permissions()


