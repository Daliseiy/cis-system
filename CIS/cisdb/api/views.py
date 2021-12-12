from rest_framework.generics import ListAPIView
from .serializers import CitizenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers
from cisdb.models import Citizen
from cisdb.face_match import identify_citizen
import json

class DataEndpoint(ListAPIView):
    queryset = Citizen.objects.all()
    serializer_class  = CitizenSerializer


@api_view(['POST'])
def find_citizen(request):
    if request.method == "POST":
        print(request.data["file"])
        result = identify_citizen(request.data["file"])
        if result=="Unknown":
            return Response({"data": "No match found"})
        else:
            names = result.split()
            full_name = ' '.join(names)
            qs = Citizen.objects.filter(first_name=names[1],surname=names[0],other_name=names[2])
            qs_json = serializers.serialize('json',qs)
            return HttpResponse(qs_json)
