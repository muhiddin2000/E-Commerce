from rest_framework import serializers, status, fields
from .models import *
from rest_framework.response import Response
from .models import Reklama


class ReklamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = ['id', 'name', 'image', 'description', 'viewed']
