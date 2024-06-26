from django.urls import path

from requests.views import RequestListAPIView, RequestCreateAPIView, RequestReadAPIView, RequestUpdateAPIView, \
    RequestDeleteAPIView, PassengerRequestListAPIView, RequestStatusListAPIView, RequestChangeStatusUpdateAPIView, \
    RequestDistributionAPIView

urlpatterns = [
    path("list", RequestListAPIView.as_view(), name="request-list"),
    path("create", RequestCreateAPIView.as_view(), name="request-create"),
    path("<int:pk>", RequestReadAPIView.as_view(), name="request-detail"),
    path("edit/<int:pk>", RequestUpdateAPIView.as_view(), name="request-edit"),
    path("delete/<int:pk>", RequestDeleteAPIView.as_view(), name="request-delete"),

    path("<int:passenger_id>/requests/", PassengerRequestListAPIView.as_view(), name="employee_request-list"),
    path("status", RequestStatusListAPIView.as_view(), name="request-status"),

    path("status/<int:pk>/change", RequestChangeStatusUpdateAPIView.as_view(), name="request-change-status"),

    path("distribution", RequestDistributionAPIView.as_view(), name="request-distribution"),

]
