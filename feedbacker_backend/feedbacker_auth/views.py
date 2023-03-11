from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from users_handler.serializers import UserSerializer


@api_view(['POST'])
def register(request):
    data = request.data
    serializer = UserSerializer(data=data)
    email = data.get('email')
    if not User.objects.filter(email=email).exists():
        serializer.is_valid(raise_exception=True)
        password = data.get('password')
        serializer.save(password=make_password(password))

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message': 'A User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
