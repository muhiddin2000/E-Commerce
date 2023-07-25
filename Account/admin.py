from django.contrib import admin
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email']