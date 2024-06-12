from rest_framework import generics

from employee.models import Employee
from employee.serializers import EmployeeSerializer
from requests.models import Request
from requests.serializers import RequestDetailSerializer


class EmployeeRequestListAPIView(generics.ListAPIView):
    serializer_class = RequestDetailSerializer

    def get_queryset(self):
        employee_id = self.kwargs.get('employee_id')
        if employee_id is not None:
            return Request.objects.filter(employee__id=employee_id)
        else:
            return Request.objects.none()


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeReadAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
