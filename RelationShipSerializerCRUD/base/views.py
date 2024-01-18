from django.shortcuts import render
from .models import Actors,Movie
from .serializers import ActorSerializer,MovieSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ActorCRUD(ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class MovieCRUD(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
