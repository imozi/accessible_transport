from rest_framework import generics

from requests.models import Request
from requests.serializers import RequestSerializer, RequestDetailSerializer


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
