from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_detail(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


# def generateNewApiKey():
#     return str(uuid.uuid4())
