from django.urls import path

from passenger.views import PassengerListAPIView, PassengerCreateAPIView, PassengerReadAPIView, PassengerDeleteAPIView, \
    PassengerUpdateAPIView

urlpatterns = [
    path("passenger/list", PassengerListAPIView.as_view(), name="passenger-list"),
    path("passenger/create", PassengerCreateAPIView.as_view(), name="passenger-create"),
    path("passenger/<int:pk>", PassengerReadAPIView.as_view(), name="passenger-detail"),
    path("passenger/edit/<int:pk>", PassengerUpdateAPIView.as_view(), name="passenger-edit"),
    path("passenger/delete/<int:pk>", PassengerDeleteAPIView.as_view(), name="passenger-delete"),

]
