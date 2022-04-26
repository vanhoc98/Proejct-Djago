from django.db import models
from products.models import *
# Create your models here.

class cart(models.Model):
	cart_id = models.AutoField(primary_key = True)
	infor_name = models.CharField(max_length = 50, blank = True, null = True)
	infor_address = models.CharField(max_length = 200, blank = True, null = True)
	infor_phone = models.CharField(max_length = 20, blank = True, null = True)

	
	# def __str__(self):
	# 	return self.infor_name
	# def __str__(self):
	# 	return self.infor_address
	# def __str__(self):
	# 	return self.infor_phone

class cartItem(models.Model):
	cart_id = models.ForeignKey(cart, on_delete = models.CASCADE)
	prod_id = models.ForeignKey(product, on_delete = models.CASCADE)
