from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name 		= models.CharField(max_length=255)
	username	= models.CharField(max_length=255)
	email 		= models.CharField(max_length=255)
	hashed_pwd	= models.CharField(max_length=255)
	created_at	= models.DateField(auto_now_add=True)

class Book(models.Model):
	title		= models.CharField(max_length=255)
	author		= models.CharField(max_length=255)

class Review(models.Model):
	score		= models.IntegerField()
	text 		= models.CharField(max_length=255)
	created_at  = models.DateField(auto_now_add=True)
	user		= models.ForeignKey(User)
	book		= models.ForeignKey(Book)