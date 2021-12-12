from rest_framework import serializers
from cisdb.models import Citizen


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model =Citizen
        fields = "__all__"