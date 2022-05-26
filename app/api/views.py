from django.http import response
from django.shortcuts import get_list_or_404, render

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .serializers import *

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)


    def post(self, request):
        response = {
            'access': 'None',
            'refresh': 'None'
        }
        status_code = None
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        try:
            response['access'] = serializer.data['access']
            response['refresh'] = serializer.data['refresh']
            status_code = status.HTTP_200_OK
        except:
            status_code = status.HTTP_404_NOT_FOUND

        return Response(response, status=status_code)