from django.shortcuts import render

import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer


class UserAPIView(APIView):
    def post(self, request):
        pass
