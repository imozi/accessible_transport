from django.urls import path

from employee.views import EmployeeRequestListAPIView, EmployeeListAPIView, EmployeeReadAPIView, EmployeeCreateAPIView, \
    EmployeeUpdateAPIView, EmployeeDeleteAPIView, EmployeesWithRequestsAPIView

urlpatterns = [
    path("<int:employee_id>/requests/", EmployeeRequestListAPIView.as_view(), name="employee_request-list"),

    path("list", EmployeeListAPIView.as_view(), name="employee_list"),
    path("create", EmployeeCreateAPIView.as_view(), name="employee_create"),
    path("<int:pk>", EmployeeReadAPIView.as_view(), name="employee_read"),
    path("edit/<int:pk>", EmployeeUpdateAPIView.as_view(), name="employee_update"),
    path("delete/<int:pk>", EmployeeDeleteAPIView.as_view(), name="employee_delete"),

    path('analytics', EmployeesWithRequestsAPIView.as_view(), name='employees-with-requests'),
]
