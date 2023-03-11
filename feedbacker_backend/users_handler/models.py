from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

class User(AbstractUser):
  email = models.EmailField(unique=True, null=False, blank=False);
  apiKey = models.UUIDField(default=uuid.uuid4, editable=True, unique=True);
  created_at = models.DateTimeField(auto_now_add=True);
  updated_at = models.DateTimeField(auto_now=True);

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []