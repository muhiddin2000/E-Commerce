from django.contrib import admin
from .models import Reklama


# Register your models here.
@admin.register(Reklama)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_show', 'name', 'image', 'description', 'viewed']
