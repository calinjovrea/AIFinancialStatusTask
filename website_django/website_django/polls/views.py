import json
import requests

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..serializers import PersonSerializer, PersonIncomeSerializer
from ..models import Person

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated !'}
        return Response(content)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


class PersonIncomeView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		person = Person.objects.get(id=request.data['id'])

		person_dict = {
			'age': person.age,
			'workSector': person.workSector,
			'education': person.education,
			'educationNum': person.educationNum,
			'statusMarriage': person.statusMarriage,
			'career': person.career,
			'relationship': person.relationship,
			'race': person.race,
			'sex': person.sex,
			'gainedCapital': person.gainedCapital,
			'lostCapital': person.lostCapital,
			'hoursPerWeek': person.hoursPerWeek,
			'country': person.country
		}

		person_income_data = json.dumps({"signature_name": "predict","instances":[person_dict]})
		person_income_data = str(person_income_data).replace("'",'"')
		r = requests.post("http://localhost:8501/v1/models/financialstatus/versions/1:predict", data=person_income_data)

		result = r.json()

		return Response({'result': result['predictions'][0]['classes'][0]})

