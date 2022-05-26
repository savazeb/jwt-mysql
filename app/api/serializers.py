from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import CustomUser

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginSerializer(serializers.Serializer):

    id = serializers.CharField(max_length=7)
    password = serializers.CharField(max_length=128, write_only=True)
    refresh = serializers.CharField(max_length=260, read_only=True)
    access = serializers.CharField(max_length=260, read_only=True)

    def validate(self, data):
        
        id = data.get('id', None)
        password = data.get('password', None)
        user = authenticate(id=id, password=password)
        
        if user is None:
            return {}
        
        token = RefreshToken.for_user(user)    
        
        response = {
            'id' : id,
            'access': str(token.access_token),
            'refresh': str(token),
        }
        return response
