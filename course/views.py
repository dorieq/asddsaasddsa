from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        return Response([])

    def post(self, request, *args, **kwargs):
        return Response("Okay")

    def put(self, request, *args, **kwargs):
        return Response("Okay")
