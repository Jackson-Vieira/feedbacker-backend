from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4;

class User(AbstractUser):
  apiKey = models.UUIDField(default=uuid4, editable=False, unique=True);
  created_at = models.DateTimeField(auto_now_add=True);
  updated_at = models.DateTimeField(auto_now=True);