from django.urls import path

from .views import DietView, ActivityInfoView

urlpatterns = [
    path("diet/", DietView.as_view()),
    path("info/", ActivityInfoView.as_view()),
]
