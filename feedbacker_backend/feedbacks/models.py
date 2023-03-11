from django.db import models

from users_handler.models import User
from users_handler.models import ApiKey

class FeedbackType(models.TextChoices):
    ISSUE = 'ISSUE', 'Issue'
    IDEA = 'IDEA', 'Idea'
    OTHER = 'OTHER', 'Other'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    apiKey = models.ForeignKey(ApiKey, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    fingersprint = models.CharField(max_length=1000, null=True, blank=True)
    device = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    page = models.URLField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=100, choices=FeedbackType.choices, black=False, null=False)

    def __str__(self):
        return f'{self.user} - {self.text}'