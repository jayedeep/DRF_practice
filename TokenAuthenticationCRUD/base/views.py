from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from .custom_permission import CustomPermission
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class StudentCrud(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CustomToken(ObtainAuthToken):

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.id,
            'email':user.email
        })