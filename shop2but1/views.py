from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse
from products.models import *
from carts.models import *

def home(request):
	cate = category.objects.all()
	prod = product.objects.all()
	context = {
		'category' : cate,
		'product' : prod
	}
	return render(request, 'home.html', context)