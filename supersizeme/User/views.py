from django.http import Http404
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from User.models import User
import json

def userLogin(request, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    return HttpResponse("Logged In :D")
    #Render the user overview page

def updateUser(request, username):
    data = json.loads(request.body)
    url = data['age'];
    weight = data['weight']
    HttpResponse(url, weight)
    # userName = request.REQUEST.get('username', '')
    # age = request.REQUEST.get('age', '')
    # gender = request.REQUEST.get('gender', '')
    # height = request.REQUEST.get('height', '')
    # weight = request.REQUEST.get('weight', '')
    # activityLevel = request.REQUEST.get('activityLevel', '')

    if username:
        user = User.objects.get(username = username)
        if user:
            user.username = username
            user.age = 0
            user.gender = 0
            user.height = 0
            user.weight = 0
            user.activityLevel = 0
            user.save()
        else:
            #Create the User if they do not exist, like on sign-up.
            User.objects.create(
            userName = username, 
            age = 1, 
            gender = 1, 
            height = 1, 
            weight = 1, 
            activityLevel = 1)
    else:
        raise Http404("Username wasn't provided")

def getUserDetails(request, username):
    username = username
    try:
        user = User.objects.get(username = username)
        response = {'name': user.username,
                    'age': user.age,
                    'gender': user.gender,
                    'height': user.height,
                    'weight': user.weight,
                    'activityLevel': user.activityLevel}
        return JsonResponse(response, safe = False)
    except User.DoesNotExist:
        raise Http404("User does not exist")
