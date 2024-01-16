from rest_framework import serializers
from .models import Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...
        print(">>>>>>",token)
        return token
