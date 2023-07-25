from django.shortcuts import render
from .serializers import ReklamaSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Reklama


# Create your views here.
class ReklamaViewset(ModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer
