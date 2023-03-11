from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken import Token

from users_handler.models import User;
from users_handler.serializers import UserSerializer

def get_token(user):
    return Token.objects.create(user=user)
    
@api_view(['POST'])
def login(request):
    data = request.data
    user = User.objects.get(email=data['email'])
    if user.check_password(data['password']):
        token = get_token(user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
