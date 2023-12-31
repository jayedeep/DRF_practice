from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class StudentCRUDView(APIView):

    def get(self,request,id=None,format=None):
        if id:
            student = get_object_or_404(Student, id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializers = StudentSerializer(students, many=True)
            return Response(serializers.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res = {'msg': 'Student Creation Failed', 'errors': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Updated Successfully'}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {'msg': 'Student Update Failed', 'errors': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id,format=None):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student partially Updated Successfully'}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {'msg': 'Student partially Update Failed', 'errors': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id,format=None):
        student = Student.objects.filter(id=id)
        student.delete()
        res = {'msg': 'Student Deleted'}
        return Response(res, status=status.HTTP_200_OK)

