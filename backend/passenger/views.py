from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from passenger.models import Passenger, PassengerCategory
from passenger.serializers import PassengerSerializer, CategorySerializer


class PassengerListAPIView(generics.ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerCreateAPIView(generics.CreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerReadAPIView(generics.RetrieveAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerUpdateAPIView(generics.UpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerDeleteAPIView(generics.DestroyAPIView):
    queryset = Passenger.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    queryset = PassengerCategory.objects.all()
    serializer_class = CategorySerializer


class PassengerSearchAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('second_name', openapi.IN_QUERY, description="Passenger second name",
                              type=openapi.TYPE_STRING),
        ],
        responses={200: PassengerSerializer}
    )
    def get(self, request):
        param = request.query_params.get('second_name')
        if param:
            try:
                queryset = Passenger.objects.get(second_name=param)
                serializer = PassengerSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Passenger.DoesNotExist:
                return Response({"error": "Passenger not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Parameter second_name is required"}, status=status.HTTP_400_BAD_REQUEST)