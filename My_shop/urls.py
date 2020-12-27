from django.urls import path
from . import views

app_name = 'my_shop'
urlpatterns = [
	path('',views.begin, name = 'begin'),

	path('shop',views.shop, name = 'shop'),
	path('shop/add/<int:item_id>',views.add_item, name = 'add_item'),
	path('basket',views.basket, name = 'basket'),
	path('shop/remove/<int:item_id>',views.remove_item, name = 'remove_item'),

	path('register',views.register, name = 'register'),
	path('register/create',views.create, name = 'create'),
	path('log_in',views.log_in, name = 'log_in'),
	path('log_in/check',views.check, name = 'check'),
	path('log_out',views.log_out, name = 'log_out'),
]