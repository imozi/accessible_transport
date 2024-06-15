from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from requests.models import Request, RequestStatus
from requests.serializers import RequestSerializer, RequestDetailSerializer, RequestStatusSerializer, \
    RequestChangeStatusSerializer
from requests.services import request_distribution


class RequestListAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestDetailSerializer


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestReadAPIView(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestDetailSerializer


class RequestUpdateAPIView(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDeleteAPIView(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PassengerRequestListAPIView(generics.ListAPIView):
    serializer_class = RequestDetailSerializer

    def get_queryset(self):
        passenger_id = self.kwargs.get('passenger_id')
        if passenger_id is not None:
            return Request.objects.filter(passenger__id=passenger_id)
        else:
            return Request.objects.none()


class RequestStatusListAPIView(generics.ListAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer


class RequestChangeStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestChangeStatusSerializer


class RequestDistributionAPIView(APIView):
    def get(self, request):
        try:
            request_distribution()
            return Response(status=status.HTTP_200_OK, data={"success": "Request distribution started"})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=e)
