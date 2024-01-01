from django.shortcuts import render,get_object_or_404
from rest_framework.viewsets import ViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentCRUDView(ViewSet):
    lookup_field = 'id'

    def list(self,request):
        print("***************************************************")
        print("basename:",self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data)

    def retrieve(self,request,id=None):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res = {'msg': 'Student Creation Failed', 'errors': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,id=None):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Updated Successfully'}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {'msg': 'Student Update Failed', 'errors': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,id=None):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Updated Successfully'}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {'msg': 'Student Update Failed', 'errors': serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,id=None):
        student = Student.objects.filter(id=id)
        student.delete()
        res = {'msg': 'Student Deleted'}
        return Response(res,status = status.HTTP_200_OK)

