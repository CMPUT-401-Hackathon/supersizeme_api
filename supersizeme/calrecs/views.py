#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from User.models import User
# Create your views here.

def calrecs(request,username):
    # Get User stats by username
    #UserStats = Question.objects.order_by('-pub_date')[:5]
    try:
        user = User.objects.get(username=username)
        age = user.age
        sex = user.gender
        height = user.height
        weight = user.weight
        activityLevel = user.activityLevel

        # 0 male, 1 female
        BMR = 0
        if sex == 0:
            # Harris Benedict kg cm
            # 10 ⨉ weight (kg) + 6.25 ⨉ height (cm) – 5 ⨉ age (years) + 5
            BMR = 10*weight + 6.25*height - 5 * int(age) + 5

        elif sex == 1:
            # Harris Benedict kg cm
            # 10 ⨉ weight (kg) + 6.25 ⨉ height (cm) – 5 ⨉ age (years) – 161
            BMR = 10*weight + 6.25*height - 5*int(age) - 161
        
        caloricIntake = 0
        if activityLevel == 1:
            # Sedentary BMR Calculation
            # Desk job, sitting most of the day
            caloricIntake = BMR * 1.2
        elif activityLevel == 2:
            # Light Activity BMR Calculation
            # Mostly sedentary, some walking and light movement
            caloricIntake = BMR * 1.375
        elif activityLevel == 3:
            # moderate Activity BMR Calculation
            # Some walking and light movement for a fwew hours
            caloricIntake = BMR * 1.55
        elif activityLevel == 4:
            # Active BMR Calculation
            # Most of the day on feet and walking
            caloricIntake = BMR * 1.725
        elif activityLevel == 5:
            # Very active bmr calculation
            # Labor job
            caloricIntake = BMR * 1.9
        
        caloriesFromCarbohydrates = caloricIntake * 0.53
        caloriesFromFat = caloricIntake * 0.20
        caloriesFromProtein = caloricIntake * 0.27

        Carbohydrates = caloriesFromCarbohydrates * .25
        Fat = caloriesFromFat * 0.11111111
        Protein = caloriesFromProtein * 0.25

        nutritionalRecommendations = {
            "calories":caloricIntake,
            "protein":Protein,
            "carbs":Carbohydrates,
            "fats":Fat
        }

        return JsonResponse(nutritionalRecommendations)

    except User.DoesNotExist:
        print("Username does not exist.")
    
    