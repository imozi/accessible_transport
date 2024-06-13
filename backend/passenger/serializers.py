from rest_framework import serializers

from passenger.models import Passenger, PassengerCategory


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["id", "first_name", "second_name", "patronymic", "phone", "category", "phone", "gender",
                  "is_pacemaker", "description"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCategory
        fields = "__all__"