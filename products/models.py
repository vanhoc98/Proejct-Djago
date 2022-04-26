from django.db import models
# Create your models here.

class category(models.Model):
	cate_id = models.AutoField(primary_key = True)
	cate_name = models.CharField(max_length = 100)

	def __str__(self):
		return self.cate_name

class product(models.Model):
	prod_id = models.AutoField(primary_key = True)
	cate_id = models.ForeignKey(category, on_delete = models.CASCADE)
	prod_name = models.CharField(max_length = 100)
	prod_price = models.DecimalField(max_digits=6, decimal_places=3)
	prod_description = models.TextField()
	prod_imgage = models.CharField(max_length = 30)
	prod_imgage_detail = models.CharField(max_length = 50, null = True)
	prod_status = models.BooleanField(default = True)


