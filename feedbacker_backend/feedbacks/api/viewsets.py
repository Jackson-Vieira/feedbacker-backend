from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from .filters import FeedbacksFilter
from ..models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = FeedbacksFilter

    def get_queryset(self):
        """ Only feedbacks from the user currently logged in are returned"""
        return self.queryset.filter(user=self.request.user)

    # Pagination
    # Ordering
    # Throttling
    