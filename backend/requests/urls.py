from django.urls import path

from requests.views import RequestListAPIView, RequestCreateAPIView, RequestReadAPIView, RequestUpdateAPIView, \
    RequestDeleteAPIView

urlpatterns = [
    path("list", RequestListAPIView.as_view(), name="request-list"),
    path("create", RequestCreateAPIView.as_view(), name="request-create"),
    path("<int:pk>", RequestReadAPIView.as_view(), name="request-detail"),
    path("edit/<int:pk>", RequestUpdateAPIView.as_view(), name="request-edit"),
    path("delete/<int:pk>", RequestDeleteAPIView.as_view(), name="request-delete"),

]
