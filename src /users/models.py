from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class User(AbstractUser):
  email = models.EmailField(unique=True, null=False, blank=False);
  created_at = models.DateTimeField(auto_now_add=True);
  updated_at = models.DateTimeField(auto_now=True);

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def create_api_key(self):
    return ApiKey.objects.create(user=self)

class ApiKey(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
  apiKey = models.UUIDField(default=uuid.uuid4, editable=True, unique=True);
  created_at = models.DateTimeField(auto_now_add=True);
  updated_at = models.DateTimeField(auto_now=True);

  def __str__(self):
    return self.apiKey




