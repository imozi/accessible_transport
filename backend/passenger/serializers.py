from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from passenger.models import Passenger, PassengerCategory


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["id", "first_name", "second_name", "patronymic", "phone", "category", "phone", "gender",
                  "is_pacemaker", "description"]


class PassengerDetailSerializer(PassengerSerializer, serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='code', read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCategory
        fields = "__all__"
