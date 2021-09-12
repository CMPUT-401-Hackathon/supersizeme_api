import json
from django.http import Http404
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from User.models import User

def userLogin(request, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    #Render the user overview page
    return HttpResponse(status=200)

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