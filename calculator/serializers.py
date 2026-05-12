from rest_framework import serializers


class NutritionSerializer(serializers.Serializer):
    protein = serializers.FloatField()
    fats = serializers.FloatField()
    carbs = serializers.FloatField()
    total_calories = serializers.FloatField()
