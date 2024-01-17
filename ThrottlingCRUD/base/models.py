from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.DateField(default=datetime.today)