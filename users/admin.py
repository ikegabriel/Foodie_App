from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'is_active', 'email_confirmed']

admin.site.register(CustomUser, CustomUserAdmin)