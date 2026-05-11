from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    UserCreateSerializer,
    UserUpdateSerializer,
    UserListSerializer,
    UserRetrieveSerializer,
)
from .permissions import IsOwner


# get users list view
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]


# get user profile view
class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


# view for register user
class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer


# view for update user
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


# view for user soft delete
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_active:
            instance.is_active = False
            instance.save()

            return Response("Account has been deleted.", status=status.HTTP_200_OK)

        return Response("Not found", status=status.HTTP_404_NOT_FOUND)


# view for login
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return Response(f"Token {token}", status=status.HTTP_200_OK)

        return Response(
            "Incorrect email or password!", status=status.HTTP_401_UNAUTHORIZED
        )