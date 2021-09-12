from django.http import Http404
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from User.models import User

def userLogin(request, username):
    try:
        user = User.objects.get(username = username)
        age = user.age
        gender = user.gender
        height = user.height
        weight = user.weight
        activityLevel = user.activityLevel    
    except User.DoesNotExist:
        raise Http404("User does not exist")
    
    UserReturn = {
        "user":username,
        "age":age,
        "gender":gender,
        "height":height,
        "weight":weight,
        "activityLevel":activityLevel
    }

    #Render the user overview page
    return JsonResponse(UserReturn)

def updateUser(request):
    userName = request.REQUEST.get('username', '')
    age = request.REQUEST.get('age', '')
    gender = request.REQUEST.get('gender', '')
    height = request.REQUEST.get('height', '')
    weight = request.REQUEST.get('weight', '')
    activityLevel = request.REQUEST.get('activityLevel', '')

    if userName:
        user = User.objects.get(username = userName)
        if user:
            user.age = age
            user.gender = gender
            user.height = height
            user.weight = weight
            user.activityLevel = activityLevel
            user.save()
        else:
            #Create the User if they do not exist, like on sign-up.
            User.objects.create(userName = userName, 
            age = age, 
            gender = gender, 
            height = height, 
            weight = weight, 
            activityLevel = activityLevel)