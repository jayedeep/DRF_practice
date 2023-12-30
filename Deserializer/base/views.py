from django.shortcuts import render,redirect,get_object_or_404
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_student(request,id):
    student = get_object_or_404(Student,id=id)
    serializer = StudentSerializer(student)
    data = serializer.data
    # json_data = JSONRenderer().render(data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(data,safe =False)


def all_student(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    data = serializer.data
    # json_data = JSONRenderer().render(data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(data,safe=False)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        bytes_to_string = io.BytesIO(json_data)
        python_data = JSONParser().parse(bytes_to_string)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Stundent Created'}
            return JsonResponse(res,safe = False)
        else:
            res = {'msg': 'Stundent Creation Failed','errors':serializer.errors}
            return JsonResponse(res, safe=False)
    else:
        return redirect('all_student')