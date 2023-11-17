from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_fields = {'password': {'write_only : True'}}

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], validated_data['email'],validated_data['password'])
            return user


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User


# class ForegetPasswordSerializer(serializers.Serializer):
#
#     email = serializers.EmailField()
#
#     def validate_email(self, value):
#         if not User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("User with this email does not exist.")
#         return value

