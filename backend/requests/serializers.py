from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from passenger.serializers import PassengerDetailSerializer
from requests.models import Request, RequestStatus


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class RequestDetailSerializer(serializers.ModelSerializer):
    # passenger = serializers.SerializerMethodField()
    passenger = PassengerDetailSerializer(many=False)

    category = SlugRelatedField(slug_field='code', read_only=True)
    status = SlugRelatedField(slug_field='status', read_only=True)
    from_station = SlugRelatedField(slug_field='name_station', read_only=True)
    to_station = SlugRelatedField(slug_field='name_station', read_only=True)
    employee = SlugRelatedField(slug_field='full_name', read_only=True)

    class Meta:
        model = Request
        fields = "__all__"

    # def get_passenger(self, obj):
    #     passenger = f"{obj.passenger.second_name} {obj.passenger.first_name} {obj.passenger.patronymic}"
    #     return passenger


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = "__all__"


class RequestChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("status",)
