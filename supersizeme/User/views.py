import json
from django.http import Http404
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User

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
    data = json.loads(request.body.decode())
    userName = data["username"]
    age = data["age"]
    height = data["height"]
    gender = data["gender"]
    weight = data["weight"]
    activityLevel = data["activityLevel"]

    if userName:
        #Create the User if they do not exist, like on sign-up.
        User.objects.create(username = userName, 
        age = age, 
        gender = gender, 
        height = height, 
        weight = weight, 
        activityLevel = activityLevel)
        return HttpResponse(status=201)
    return HttpResponse(status=400)