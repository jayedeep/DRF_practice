from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'bod']
        extra_kwargs = {'email':{'read_only':True}}



    def to_representation(self,instance):
        customization = super().to_representation(instance)
        customization['name_with_email'] = instance.name + ' ' + instance.email
        return customization