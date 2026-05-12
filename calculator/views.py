from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .util_classes import NutritionCalculator
from .serializers import NutritionSerializer


class DietView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        gender = user.gender
        weight = user.weight
        height = user.height
        age = user.age
        activity_status = user.activity_status
        target = user.target

        bmr = NutritionCalculator.calculate_bmr(gender, weight, height, age)
        tdee = NutritionCalculator.calculate_tdee(bmr, activity_status)
        daily_calories = NutritionCalculator.calculate_daily_calories(tdee, target)
        macros = NutritionCalculator.calculate_macros(
            daily_calories, target, gender, weight
        )

        response = NutritionSerializer(macros).data

        return Response(response, status=status.HTTP_200_OK)


class ActivityInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(NutritionCalculator.get_info(), status=status.HTTP_200_OK)