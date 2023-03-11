from django_filters import rest_framework as filters

from ..models import Feedback

class FeedbacksFilter(filters.FilterSet):
    class Meta:
        model = Feedback
        fields = ['type']
