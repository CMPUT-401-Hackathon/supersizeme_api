from django.http import Http404
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from models import User

def createUser(request):
    userName = request.REQUEST.get('username', '')
    # Check if user already existed
    if userName:
        user = User.objects.get(username = userName)
        if user:
            return HttpResponse("Username already exists")
        else:
            User.objects.create(username = userName)
            #Render the first login page
    else:
        return HttpResponse("Request is Empty")

def userLogin(request, username):
    try:
        user = User.objects.get(username = username)
    except user.DoesNotExist:
        raise Http404("User does not exist")
    #return the user overview page

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
            raise Http404("User does not exist")
        






