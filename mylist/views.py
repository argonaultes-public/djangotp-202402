from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseServerError
from django.views import generic
from .models import ShopList, ShopListItem

# Create your views here.

def index(request):
    return HttpResponse('Index of my list')

def shopping_list(request):
    shopping_list = ShopList.objects.all()
    # template loader
    template = loader.get_template('shoplist.html')
    # context
    context = { 'shoplists': shopping_list}
    return HttpResponse(template.render(context, request))

def shopping_list_details_v2(request, listid):
    try:
        shopping_list = ShopList.objects.get(id = listid)
        context = {
            'shoplist': shopping_list,
            'shoplistitems': shopping_list.shoplistitem_set.all(),
        }
        return render(request, 'listdetails.html', context)
    except:
        return HttpResponseServerError('listid not found')

def shopping_list_details(request, listid):
    shopping_list = ShopList.objects.filter(id = listid) # QuerySet

    context = {
        'shoplist': None,
        'shoplistitems': None,
    }
    if len(shopping_list) == 1:
        shopping_list_items = ShopListItem.objects.filter(shop_list = shopping_list[0])
        context['shoplist'] = shopping_list[0]
        context['shoplistitems'] = shopping_list_items
    return render(request, 'listdetails.html', context)

class ShoppingListView(generic.ListView):
    model = ShopList
    template_name = 'shoplist.html'
    context_object_name = 'shoplists'