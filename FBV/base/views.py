from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students,many=True)
    return Response(serializers.data)

@api_view(['GET','POST','DELETE','PUT'])
def student_crud(request,id=None):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Student Created'}
            return Response(res,status = status.HTTP_201_CREATED)
        else:
            res = {'msg': 'Student Creation Failed','errors':serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        student = get_object_or_404(Student,id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Student Updated Successfully'}
            return Response(res,status = status.HTTP_200_OK)
        else:
            res = {'msg': 'Student Update Failed','errors':serializer.errors}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student = Student.objects.filter(id=id)
        student.delete()
        res = {'msg': 'Student Deleted'}
        return Response(res,status = status.HTTP_200_OK)

