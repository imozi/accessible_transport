from django.urls import path

from metro.views import MetroRouteListAPIView, StationListAPIView

urlpatterns = [
    path("path", MetroRouteListAPIView.as_view(), name="metro_route"),
    path("stations", StationListAPIView.as_view(), name="metro_stations"),
]
