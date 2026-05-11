from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserCreateSerializer, UserUpdateSerializer, UserListSerializer, UserRetrieveSerializer


# view for get CRSF
@api_view(['GET'])
def get_csrf(request):
    token = get_token(request)
    return Response(token)

# get users list view
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

# get user profile view
class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer

# view for register user
class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

# view for update user
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer