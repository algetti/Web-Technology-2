from django.db import models

class Item(models.Model):
	name = models.CharField(max_length = 100)
	detail = models.CharField(max_length = 2000)
	price =  models.PositiveIntegerField()

	def __str__(self):
		return f'{self.name}; price = {self.price}'

class User(models.Model):
	name = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return f'{self.id}. {self.name}'
