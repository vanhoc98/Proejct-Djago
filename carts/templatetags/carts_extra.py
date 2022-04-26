from django import template
from products.models import *
from carts.models import *
from decimal import *

register = template.Library()

@register.filter
def total(item):
	total = 0
	for i in item:
		total += i.prod_price
	return total

@register.filter
def sumtotal(item):
	total = 0
	for i in item:
		total += i.prod_price
	return total + Decimal(30.000)