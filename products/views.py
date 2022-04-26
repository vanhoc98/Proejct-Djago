from django.shortcuts import render
from django.http import Http404
from django.template import loader

from .models import *
# Create your views here.

from django.http import HttpResponse

def product_detail(request, prod_id):
	try:
		prod = product.objects.get(pk=prod_id)
	except product.DoesNotExist:
		raise Http404("hehee")
	return render(request, 'store/product_detail.html', {'prod': prod})

