from django.http import response
from django.shortcuts import get_list_or_404, render

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .serializers import *

class UserLoginView(RetrieveAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'sucess': 1,
            'status_code': status.HTTP_200_OK,
            'message': 'Login in succesfull',
            'refresh': serializer.data['refresh'],
            'token': serializer.data['access'],
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)