from django.http import HttpResponse, JsonResponse
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
    item = Item.objects.get(name=name)
    return JsonResponse(item.json_representation())
