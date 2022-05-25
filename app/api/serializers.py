from rest_framework import serializers
from .models import CustomUser

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = {'first_name', 'last_name'}


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=260)
    password = serializers.CharField(max_length=128, write_only=True)
    refresh = serializers.CharField(max_length=260, read_only=True)
    access = serializers.CharField(max_length=260, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        
        token = RefreshToken.for_user(user)
        
        response = {
            'email' : email,
            'refresh': str(token),
            'access': str(token.access_token),
        }
        return response
