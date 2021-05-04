from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class LogOutView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
