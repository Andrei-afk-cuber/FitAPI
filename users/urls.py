from django.urls import path

from .views import UserCreateView, UserUpdateView, UserListView, UserProfileView, get_csrf

urlpatterns = [
    path('csrf-token/',get_csrf),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
]
