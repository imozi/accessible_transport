from rest_framework import serializers

from metro.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id_station', 'name_station']
