from rest_framework import serializers, status, fields
from .models import *
from rest_framework.response import Response
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'image', 'description', 'cost', 'discount', 'viewed']
