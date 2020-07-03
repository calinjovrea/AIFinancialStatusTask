from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'age','workSector', 'education', 'educationNum', 'statusMarriage', 'career', 'relationship', 'race', 'sex', 'gainedCapital', 'lostCapital', 'hoursPerWeek', 'country')