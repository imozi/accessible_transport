from django.urls import path

from passenger.views import PassengerListAPIView, PassengerCreateAPIView, PassengerReadAPIView, PassengerDeleteAPIView, \
    PassengerUpdateAPIView

urlpatterns = [
    path("list", PassengerListAPIView.as_view(), name="passenger-list"),
    path("create", PassengerCreateAPIView.as_view(), name="passenger-create"),
    path("<int:pk>", PassengerReadAPIView.as_view(), name="passenger-detail"),
    path("edit/<int:pk>", PassengerUpdateAPIView.as_view(), name="passenger-edit"),
    path("delete/<int:pk>", PassengerDeleteAPIView.as_view(), name="passenger-delete"),

]
