from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse
from products.models import *
from carts.models import *

def carts(request):
	item = product.objects.filter(cartitem__cart_id=1)

	context = {
		'item' : item,
		'count' : item.count()
	}

	return render(request, 'store/carts.html', context)

def checkout(request):
    return render(request, 'store/checkout.html')
