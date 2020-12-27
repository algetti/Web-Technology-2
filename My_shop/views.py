from django.shortcuts import render
from .models import Item,User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import redis

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,charset="utf-8",decode_responses=True, db=0)


# Create your views here.

def begin(request):
	return HttpResponseRedirect(reverse('my_shop:shop'))

def get_User():
	ID = redis_instance.get('id')
	if ID: 
		return User.objects.get(id = int(ID))
	else:
		return False

def get_items_in_basket():
	items = redis_instance.get('basket')
	if items:
		return items.split(',')
	else:
		return False

def set_items_in_basket(array):
	array = [str(i) for i in array]
	redis_instance.set('basket',','.join(array))

def add_item_to_basket(id):
	items = get_items_in_basket()
	if items:
		items.append(id)
	else:
		items = f'{id}'
	set_items_in_basket(items)

def delete_item_from_busket(id):
	items = get_items_in_basket()
	for i in range(len(items)):
		if items[i] == f'{id}':
			del items[i]
			break
	set_items_in_basket(items)

def shop(request):
	items = Item.objects.order_by('name')
	return render(request, 'pages/shop.html',{'items': items,'login': get_User()})

def add_item(request,item_id):
	add_item_to_basket(item_id)
	return HttpResponseRedirect(reverse('my_shop:shop'))

def basket(request):
	items = get_items_in_basket()
	if items:
		basket_items = []
		for i in items:
			temp = Item.objects.get(id = i)
			basket_items.append({
				'id':temp.id,
				'name':temp.name,
				'detail':temp.detail,
				'price':temp.price,
			})
		return render(request, 'pages/basket.html',{'items': basket_items,'login': get_User()})
	else:
		return render(request, 'pages/basket.html',{'items': False,'login': get_User()})

def remove_item(request,item_id):
	delete_item_from_busket(item_id)
	return HttpResponseRedirect(reverse('my_shop:basket'))






def register(request):
	return render(request, 'pages/logreg.html',{'new': True,'login': get_User()})

def create(request):
	user0 = User(
		name     = request.POST['name'    ],
		password = request.POST['password'],
	)

	user0.save()
	redis_instance.set('id', user0.id)
	return HttpResponseRedirect(reverse('my_shop:begin'))

def log_in(request):
	return render(request, 'pages/logreg.html',{'new':False,'login': get_User()})

def check(request):
	try:
		user = User.objects.get(name = request.POST['name'])
		if user.password == request.POST['password']:
			redis_instance.set('id', user.id)
			return HttpResponseRedirect(reverse('my_shop:begin'))
		else:
			return HttpResponseRedirect(reverse('my_shop:log_in'))
	except:
		return HttpResponseRedirect(reverse('my_shop:log_in'))

def log_out(request):
	redis_instance.delete('id')
	return HttpResponseRedirect(reverse('my_shop:begin'))
