from rest_framework import serializers
from .models import Student


def custom_validation(value):
    print(">>>>>>",value)
    if value[0] == 'z':
        raise serializers.ValidationError("Please Name Should not start with Z")
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,validators=[custom_validation])
    email = serializers.EmailField()

    def validate_name(self,value):
        if value in Student.objects.all().values_list('name',flat=True):
            raise serializers.ValidationError("Student with this name already exists")
        return value

    def validate_email(self, value):
        if value in Student.objects.all().values_list('email', flat=True):
            raise serializers.ValidationError("Student with this email already exists")
        return value

    def validate(self,data):
        name = data.get('name',False)
        email = data.get('email',False)
        if name.lower() != name or email.lower() != email:
            raise serializers.ValidationError("Student name or email should be in Lower case Always")
        return data

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        print(">>>>update",instance.name,instance.email,validated_data)
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance