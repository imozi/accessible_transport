import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from metro.models import Station
from metro.serializers import StationSerializer
from metro.shortest_path import get_shortest_path

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
        responses={200: StationSerializer}
    )
    def get(self, request):
        from_station_id = request.GET.get('from_station')
        to_station_id = request.GET.get('to_station')
        time_start = request.GET.get('time_start')

        if from_station_id and to_station_id:
            try:

                from_station = Station.objects.get(id_station=from_station_id)
                to_station = Station.objects.get(id_station=to_station_id)
                from_station_serializer = StationSerializer(from_station, context={'request': request})
                to_station_serializer = StationSerializer(to_station, context={'request': request})

                path = get_shortest_path(from_station_id, to_station_id)
                route_time = round(path["time"])

                hours = route_time // 60
                minutes = route_time % 60

                print(hours, minutes)
                start_time = datetime.datetime.strptime(time_start, '%H:%M')
                time_end = start_time + datetime.timedelta(minutes=route_time)
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
                # response_serializer = StationSerializer(data)
                return Response(data, status=status.HTTP_200_OK)
            except Station.DoesNotExist:
                return Response({'error': 'Station not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)
