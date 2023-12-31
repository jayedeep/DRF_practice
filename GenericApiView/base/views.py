from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        response = self.create(request, *args, **kwargs)

        # Customize the response
        custom_response = {
            "msg": "New student created",
            "status": status.HTTP_201_CREATED,  # or status.HTTP_200_OK if you prefer
        }

        # Return the custom response
        return Response(custom_response, status=status.HTTP_201_CREATED)


class StudentUpdateRetriveDelete(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)