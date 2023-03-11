from django.contrib import admin
from .models import User, ApiKey

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    pass