from django.urls import path

from .views import DietView

urlpatterns = [
    path("diet/", DietView.as_view()),
]
