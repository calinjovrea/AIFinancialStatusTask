from django.db import models

#● name: - Required
#● age: - Required
#● workSector: - Required
#● education: - Optional. Default: “HS-grad”
#● educationNum: - Optional. Default: 9
#● statusMarriage: - Required
#● career: - Required
#● relationship: - Required
#● race: - Optional. Default: “Other”
#● sex: - Required
#● gainedCapital: - Required
#● lostCapital: - Required
#● hoursPerWeek: - Optional. Default: 40.
#● country: Optional. Default: “United-States”

class Person(models.Model):
	name = models.CharField(max_length=256)
	age = models.IntegerField(default=0)
	