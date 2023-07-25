from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','image_show', 'name','image','description','cost','discount','viewed']
    list_filter = ['category', 'discount']
    # list_editable = ['name', 'category', 'cost', 'discount']
    search_fields = ['name', 'cost', 'description', 'discount']