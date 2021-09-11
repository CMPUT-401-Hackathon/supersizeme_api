import datetime, json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from User.models import User
from backend.models import Item
from .models import Log
# Create your views here.

def log(request, username, date):
    user = get_object_or_404(User, username=username)
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    if request.method == "GET":
        logs = list(Log.objects.filter(date=date))
        for log in logs:
            log.item = log.item.name
        print(logs)

        pass
    elif request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        item_name = data["item"]
        item = get_object_or_404(Item, name=item_name)
        amount = float(data["amount"])
        Log.objects.create(user=user, date=date, item=item, amount=amount)
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    else:
        return HttpResponse(status=400)

    return HttpResponse(status=200)

