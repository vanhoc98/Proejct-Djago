from django.urls import path
from . import views

# app_name = 'carts'
urlpatterns = [
	#path('remove/<int:cart_id>/', views.cart_add, name='cart_remove'),
	path('checkout/', views.checkout, name='checkout'),
	path('', views.carts, name='carts'),
]
