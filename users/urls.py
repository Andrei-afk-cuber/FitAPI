from django.urls import path

from .views import UserCreateView, UserUpdateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
]
