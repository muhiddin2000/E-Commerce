from django.shortcuts import render
from rest_framework import permissions

from .models import CustomUser
from .serializers import UserSerializer,UserUpdateSerializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView


# Create your views here.
class UserCreate(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserUpdate(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializers
