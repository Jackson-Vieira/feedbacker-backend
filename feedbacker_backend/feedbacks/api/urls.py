from rest_framework import routers
from .viewsets import FeedbackViewSet

router = routers.SimpleRouter()
router.register(r'feedbacks', FeedbackViewSet)