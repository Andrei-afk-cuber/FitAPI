from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer


# TODO: сделать и подключить представление для регистрации пользователей
class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [AllowAny]