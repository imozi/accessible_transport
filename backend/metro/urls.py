from django.urls import path

from metro.views import MetroRouteListAPIView

urlpatterns = [
    path("", MetroRouteListAPIView.as_view(), name="metro_route"),
]
