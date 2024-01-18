from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime

# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    lead_actor = models.ForeignKey(Actors,on_delete=models.CASCADE,related_name='movie')

    def __str__(self):
        return self.name