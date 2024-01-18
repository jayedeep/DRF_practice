from rest_framework import serializers
from .models import Actors,Movie


class ActorSerializer(serializers.ModelSerializer):
    # movie = serializers.StringRelatedField(many=True,read_only=True) # it will show the name of string fields
    # movie = serializers.PrimaryKeyRelatedField(many=True,read_only=True)  # it will show only primary key
    # movie = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')  # it will show only primary key
    movie = serializers.HyperlinkedRelatedField(many=True,view_name='movie_url-detail',read_only=True)  # it will show only primary key

    class Meta:
        model = Actors
        fields = ['id','name','character','movie']

class MovieSerializer(serializers.ModelSerializer):
    lead_actor = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Movie
        fields = ['id','name','lead_actor']