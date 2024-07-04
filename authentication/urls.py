from django.urls import path
from django.contrib import admin
from .views import *
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
     path('login/', LoginView.as_view(), name="login"),
]
# router = DefaultRouter()
# router.register('register', RegisterViewset, basename='register')
# router.register('login', LoginViewSet, basename='login')
# router.register('users', UserViewSet, basename='users')