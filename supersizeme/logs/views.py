import datetime, json
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from User.models import User
from backend.models import Item
import numbers
from .models import Log
# Create your views here.

def log(request, username, date):
    user = get_object_or_404(User, username=username)
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    if request.method == "GET":
        logs = Log.objects.filter(date=date, user=user)
        output = {}
        for log in logs:
            for key, val in log.item.json_representation().items():
                if isinstance(val, numbers.Number):
                    if key not in output:
                        output[key] = 0
                    output[key] += log.amount * val
        return JsonResponse(output)

    elif request.method == "POST":
        data = json.loads(request.body.decode())
        item_name = data["item"]
        item = get_object_or_404(Item, name=item_name)
        amount = float(data["amount"])
        Log.objects.create(user=user, date=date, item=item, amount=amount)
        return HttpResponse(status=201)
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    else:
        pass

    return HttpResponse(status=400)

def logs(request, username):
    user = get_object_or_404(User, username=username)
    logs = Log.objects.filter(user=user)
    output = {}
    for log in logs:
        for key, val in log.item.json_representation().items():
            if isinstance(val, numbers.Number):
                if key not in output:
                    output[key] = 0
                output[key] += log.amount * val
    return JsonResponse(output)