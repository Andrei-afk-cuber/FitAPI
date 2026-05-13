class NutritionCalculator:
    ACTIVITY_FACTORS = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    GOAL_FACTORS = {"loss": 0.85, "maintain": 1, "gain": 1.1}
    MACRO_RATIOS = {
        "loss": {
            "protein": 0.40,
            "fats": 0.30,
            "carbs": 0.30,
        },
        "maintain": {
            "protein": 0.30,
            "fats": 0.30,
            "carbs": 0.40,
        },
        "gain": {
            "protein": 0.30,
            "fats": 0.25,
            "carbs": 0.45,
        },
    }

    @classmethod
    def calculate_bmr(cls, gender, weight, height, age):
        "Calculate by Miffiline-San Genore"
        # for male
        if gender == "M":
            return (10 * weight) + (6.25 * height) - (5 * age) + 5
        # for female
        else:
            return (10 * weight) + (6.25 * height) - (5 * age) - 161

    @classmethod
    def get_activity_factor(cls, activity_status):
        "Transform number to coefficients"
        return cls.ACTIVITY_FACTORS[activity_status]

    @classmethod
    def calculate_tdee(cls, bmr, activity_status):
        """Total daily calorie intake"""
        factor = cls.get_activity_factor(activity_status)
        return bmr * factor

    @classmethod
    def get_goal_factor(cls, target):
        """Get coefficient by target"""
        return cls.GOAL_FACTORS[target]

    @classmethod
    def calculate_daily_calories(cls, tdee, target):
        """Calculate daily calorie intake"""
        factor = cls.get_goal_factor(target)
        return tdee * factor

    @classmethod
    def calculate_macros(cls, calories, target, gender, weight):
        """Calculate macro intake"""
        ratios = cls.MACRO_RATIOS[target]

        # calculation in grams
        protein_calories = calories * ratios["protein"]
        fat_calories = calories * ratios["fats"]
        carbs_calories = calories * ratios["carbs"]

        # calculation protein by weight
        protein_by_weight = weight * 1.8
        protein_by_percent = protein_calories / 4

        final_protein = max(protein_by_weight, protein_by_percent)

        return {
            "protein": round(final_protein, 1),
            "fats": round(fat_calories / 9, 1),
            "carbs": round(carbs_calories / 4, 1),
            "total_calories": round(calories),
        }

    @classmethod
    def get_info(cls):
        return {
            1: "Sedentary lifestyle",
            2: "Light activity 1-3 days a week",
            3: "Moderate exercise 3-5 days a week",
            4: "Intensive training 6-7 days a week",
            5: "Very intense exercise every day",
        }
