from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    UserCreateView,
    UserUpdateView,
    UserListView,
    UserProfileView,
    UserDeleteView,
    LoginView,
)


urlpatterns = [
    path("", UserListView.as_view()),
    path("<int:pk>/", UserProfileView.as_view()),
    path("register/", UserCreateView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("<int:pk>/update/", UserUpdateView.as_view()),
    path("<int:pk>/delete/", UserDeleteView.as_view()),
]
