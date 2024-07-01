from django.shortcuts import render
from rest_framework import viewsets, generics, status, views, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class RegisterView(generics.GenericAPIView):
    def get(self, request):
        return render(request, 'authentication/register.html')
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return render(request, 'authentication/login.html')


class LoginAPIView(generics.GenericAPIView):
    def get(self, request):
        return render(request, 'authentication/login.html')

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # permissions_classes = [permissions.AllowAny]
    # queryset = User.objects.all()
    # serializer_class = RegisterSerializer

    # def create(self, request):
    #     serializer = self.serializer_class(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

    #     else:
    #         return Response(serializer.errors, status=400)
