from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    email_custom = serializers.CharField(source = 'email')
    custom_name_email = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'email':{'read_only':True}}

    def get_custom_name_email(self, obj):
        # This method computes the value for the 'custom_field' in the serialized output
        return f"Custom value for {obj.email.upper()}"

    def to_representation(self,instance):
        customization = super().to_representation(instance)
        customization['name_with_email'] = instance.name + ' ' + instance.email
        return customization