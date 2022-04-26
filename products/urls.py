from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
	# product_detail/2/
	path('<int:prod_id>/', views.product_detail, name='product_detail'),
	# path('<int:prod_id>/', views.detail, name='detail'),
]
