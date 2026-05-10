from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserCreateSerializer, UserUpdateSerializer, UserListSerializer, UserRetrieveSerializer


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