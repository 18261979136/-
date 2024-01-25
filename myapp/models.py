from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField(default=20)
	phone = models.CharField(max_length=16)
	addtime = models.DateTimeField(default = datetime.now)
	
class Creep(models.Model):
	temperature = models.IntegerField(default=20)
	stress = models.IntegerField(default=20)
	speed = models.DecimalField(max_digits=10, decimal_places=10)
	addtime = models.DateTimeField(default = datetime.now)
	