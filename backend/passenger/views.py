from rest_framework import generics

from passenger.models import Passenger
from passenger.serializers import PassengerSerializer


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
