from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def get_student(request,id):
    student = get_object_or_404(Student,id=id)
    serializer = StudentSerializer(student)
    data = serializer.data
    json_data = JSONRenderer().render(data)
    return HttpResponse(json_data,content_type="application/json")


def all_student(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    data = serializer.data
    json_data = JSONRenderer().render(data)
    return HttpResponse(json_data,content_type="application/json")
