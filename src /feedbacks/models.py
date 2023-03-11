from django.db import models

from users.models import User
from users.models import ApiKey

class FeedbackType(models.TextChoices):
    ISSUE = 'ISSUE', 'Issue'
    IDEA = 'IDEA', 'Idea'
    OTHER = 'OTHER', 'Other'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    apiKey = models.ForeignKey(ApiKey, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.TextField(max_length=1000)
    fingersprint = models.CharField(max_length=1000, null=False, blank=False)
    device = models.CharField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    page = models.URLField(max_length=1000, null=False, blank=False)
    type = models.CharField(max_length=10, choices=FeedbackType.choices, blank=False, null=False)

    def __str__(self):
        return f'{self.user} - {self.text}'