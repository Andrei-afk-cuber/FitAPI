from django.contrib.auth import authenticate
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, inline_serializer
from rest_framework import status, serializers
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
@extend_schema_view(
    get=extend_schema(
        summary="Get users",
        description="Get list of users",
    )
)
class UserListView(ListAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = UserListSerializer


# get user profile view
@extend_schema_view(
    get=extend_schema(
        summary="User profile",
        description="Get user profile",
    )
)
class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsAuthenticated, IsOwner]


# view for register user
@extend_schema_view(
    post=extend_schema(
        summary="New user",
        description="Create new user",
    )
)
class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request,*args, **kwargs)


# view for update user
@extend_schema_view(
    put=extend_schema(
        summary="Update user",
        description="Updated user fully",
    ),
    patch=extend_schema(
        summary="Patch user",
        description="Update user partially",
    ),
)
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


# view for user soft delete
@extend_schema_view(
    delete=extend_schema(
        summary="Delete user",
        description="Soft user deletion (is_active=False)",
        responses={
            200: OpenApiTypes.STR,
            404: OpenApiTypes.STR,
        },
    )
)
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
    @extend_schema(
        summary="Login user",
        description="Login user and get token",
        request=inline_serializer(
            name="LoginSerializer",
            fields={
                "email": serializers.EmailField(),
                "password": serializers.CharField(),
            },
        ),
        responses={
            200: OpenApiTypes.STR,
            401: OpenApiTypes.STR,
        },
    )
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
