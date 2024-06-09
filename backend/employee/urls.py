from django.urls import path

from employee.views import EmployeeRequestListAPIView

urlpatterns = [
    path("<int:employee_id>/requests/", EmployeeRequestListAPIView.as_view(), name="employee_request-list"),
]
