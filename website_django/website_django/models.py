from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	workSector = models.CharField(max_length=50)
	education = models.CharField(max_length=50, default='HS-grad')
	educationNum = models.IntegerField(default=9)
	statusMarriage = models.CharField(max_length=15)
	career = models.CharField(max_length=30)
	relationship =models.CharField(max_length=30)
	race = models.CharField(max_length=15, default='Other')
	sex = models.CharField(max_length=15)
	gainedCapital = models.IntegerField()
	lostCapital = models.IntegerField()
	hoursPerWeek = models.IntegerField(default=40)
	country = models.CharField(max_length=50, default='United-States')
	income = models.CharField(max_length=10)