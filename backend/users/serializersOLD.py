from rest_framework import serializers
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["id", "email","user_type"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=CustomUser.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  class Meta:
    model = CustomUser
    fields = ( 'email', 'password',)
  def validate(self, attrs):
    # if attrs['password'] != attrs['password2']:
    #   raise serializers.ValidationError(
    #     {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data,instance=None):
    user = CustomUser.objects.create(
    email=validated_data['email'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user