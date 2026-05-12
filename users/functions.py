def calculate_bmr(gender, weight, height, age):
    "Calculate by Miffiline-San Genore"
    # for male
    if gender == "M":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    # for female
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161

def get_activity_factor(activity_status):
    "Transform number to coefficients"
    activity_factors = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    return activity_factors[activity_status]

def calculate_tdee(bmr, activity_status):
    """Total daily calorie intake"""
    factor = get_activity_factor(activity_status)
    return bmr * factor

def get_goal_factor(target):
    """Get coefficient by target"""
    goal_factors = {
        'weight loss': 0.85,
        'maintain': 1,
        'gain': 1.1
    }
    return goal_factors.get(target, goal_factors['maintain'])

def calculate_daily_calories(tdee, target):
    """Calculate daily calorie intake"""
    factor = get_goal_factor(target)
    return tdee * factor

def calculate_macros(calories, target, gender, weight):
    """Calculate macro intake"""
    macro_ratios = macro_ratios = {
        "loss": {
            "protein": 0.40,  # 40% белки (сохраняем мышцы)
            "fat": 0.30,      # 30% жиры
            "carbs": 0.30,    # 30% углеводы
        },
        "maintain": {
            "protein": 0.30,
            "fat": 0.30,
            "carbs": 0.40,
        },
        "gain": {
            "protein": 0.30,
            "fat": 0.25,
            "carbs": 0.45,
        }
    }

    ratios = macro_ratios.get(target, macro_ratios['maintain'])

    # calculation in grams
    protein_calories = calories * ratios['protein']
    fat_calories = calories * ratios['fat']
    carbs_calories = calories * ratios['carbs']

    # calculation protein by weight
    protein_by_weight = weight * 1.8
    protein_by_percent = protein_calories / 4

    final_protein = max(protein_by_weight, protein_by_percent)

    return {
        "protein": round(final_protein, 1),
        "fat": round(fat_calories / 9, 1),
        "carbs": round(carbs_calories / 4, 1),
        "total_calories": round(calories)
    }