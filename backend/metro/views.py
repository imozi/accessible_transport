import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from metro.models import Station
from metro.serializers import StationSerializer, MetroRouteSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class MetroRouteListAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('from_station', openapi.IN_QUERY, description="ID of the starting station",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('to_station', openapi.IN_QUERY, description="ID of the destination station",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('time_start', openapi.IN_QUERY, description="Starting time in HH:MM format",
                              type=openapi.TYPE_STRING)
        ],
        responses={200: MetroRouteSerializer}
    )
    def get(self, request):
        from_station_id = request.GET.get('from_station')
        to_station_id = request.GET.get('to_station')
        time_start = request.GET.get('time_start')
        if not from_station_id or not to_station_id or not time_start:
            return Response({'error': 'invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            from_station = Station.objects.get(id_station=from_station_id)
            to_station = Station.objects.get(id_station=to_station_id)
        except Station.DoesNotExist:
            return Response({'error': 'station not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            start_time = datetime.datetime.strptime(time_start, '%H:%M')
        except ValueError:
            return Response({'error': 'invalid time format, should be HH:MM'}, status=status.HTTP_400_BAD_REQUEST)
        from_station_serializer = StationSerializer(from_station, context={'request': request})
        to_station_serializer = StationSerializer(to_station, context={'request': request})
        from metro.shortest_path import get_shortest_path
        path = get_shortest_path(from_station_id, to_station_id)
        route_time = round(path["time"])

        if route_time < 10:
            time_end = start_time + datetime.timedelta(minutes=route_time + 5)
        elif 10 < route_time < 20:
            time_end = start_time + datetime.timedelta(minutes=route_time + 10)
        else:
            time_end = start_time + datetime.timedelta(minutes=route_time + 15)

        time_end = datetime.datetime.strftime(time_end, '%H:%M')
        data = {
            'from_station': from_station_serializer.data,
            'to_station': to_station_serializer.data,
            "path": path["stations"],
            "transfers": path["transfers"],
            "route_time": route_time,
            "time_start": time_start,
            "time_end": time_end
        }
        return Response(data, status=status.HTTP_200_OK)


class StationListAPIView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
