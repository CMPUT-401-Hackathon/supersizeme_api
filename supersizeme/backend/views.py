import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from backend.models import Item

# GET Request for food categories
def index(request):
    categories_dict = Item.objects.order_by().values('category').distinct()
    categories_dict = list(categories_dict)
    categories = []
    for adict in categories_dict:
        categories.extend(adict.values())
    
    return JsonResponse(categories, safe=False)

# GET Request for nutritional info for an item
def item_info(request, name):
    try:
        item = Item.objects.get(name=name)
        return JsonResponse(item.json_representation())
    except:
        return HttpResponseNotFound()

    

# GET Request for nutritional info for a category of items
def category_info(request, category):
    items = list(Item.objects.filter(category=category))
    if len(items) == 0:
        return HttpResponseNotFound()
    
    items_jsoned = []
    for item in items:
        items_jsoned.append(item.json_representation())
    return JsonResponse(items_jsoned, safe=False)

def delete(request, name):
    item = get_object_or_404(Item, name=name)
    item.delete()
    return HttpResponse(status=200)

def add(request, name):
    data = json.loads(request.body.decode())
    Item.objects.create(name=name, **data)
    return HttpResponse(status=201)
