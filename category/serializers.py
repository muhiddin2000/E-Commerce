from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    # bookcount = serializers.SerializerMethodField('books_soni')

    # def books_soni(self, obj):
    #     return obj.bookscount

    class Meta:
        model = Category
        fields = ['id', 'name',]
        depth = 2
