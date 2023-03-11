from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.register, name='register'),
]
