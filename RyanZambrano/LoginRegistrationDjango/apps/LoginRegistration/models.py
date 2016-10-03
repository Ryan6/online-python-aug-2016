from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name	= models.CharField(max_length=255)
	last_name	= models.CharField(max_length=255)
	email		= models.CharField(max_length=255)
	hashed_pwd 	= models.CharField(max_length=255)
	created_at 	= models.DateField(auto_now_add=True)