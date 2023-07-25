from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pogination import MyPagination
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .filter import ProductFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class ProductViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ('name', 'cost')
