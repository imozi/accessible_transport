from rest_framework import serializers

from metro.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id_station', 'name_station']


class MetroRouteSerializer(serializers.Serializer):
    from_station = StationSerializer()
    to_station = StationSerializer()
    path = serializers.ListField(child=serializers.CharField())
    transfers = serializers.ListField(child=serializers.CharField())
    route_time = serializers.IntegerField()
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
