from rest_framework import serializers
from .models import User
from .models import ApiKey

class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ['apiKey', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    api_keys = ApiKeySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'api_keys', 'created_at', 'updated_at']