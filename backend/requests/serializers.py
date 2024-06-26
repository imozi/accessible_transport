from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from employee.serializers import EmployeeSerializer
from metro.models import Station
from passenger.serializers import PassengerSerializer
from requests.models import Request, RequestStatus


class RequestSerializer(serializers.ModelSerializer):
    from_station = SlugRelatedField(queryset=Station.objects.all(), slug_field='id_station')
    to_station = SlugRelatedField(queryset=Station.objects.all(), slug_field='id_station')

    class Meta:
        model = Request
        fields = "__all__"


class RequestDetailSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=False)
    employee = EmployeeSerializer(many=True)

    category = SlugRelatedField(slug_field='code', read_only=True)
    status = SlugRelatedField(slug_field='status', read_only=True)
    from_station = SlugRelatedField(slug_field='name_station', read_only=True)
    to_station = SlugRelatedField(slug_field='name_station', read_only=True)

    class Meta:
        model = Request
        fields = "__all__"


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = "__all__"


class RequestChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("status",)
