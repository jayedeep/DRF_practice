from django.contrib import admin
from .models import Student
# Register your models here.


class StudentModel(admin.ModelAdmin):
    list_display = ['name','email','bod']
    list_editable = ['email']

admin.site.register(Student,StudentModel)