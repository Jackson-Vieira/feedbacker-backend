from rest_framework import serializers
from feedbacker_backend.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        ordering = ['-created_at']
        
