from rest_framework import generics, status
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import EmployeeSerializer, EmployeeDetailRequestsSerializer
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
    serializer_class = EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeesWithRequestsAPIView(generics.ListAPIView):
    queryset = Employee.objects.filter(requests__isnull=False).distinct()
    serializer_class = EmployeeDetailRequestsSerializer
