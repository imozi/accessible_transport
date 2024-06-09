from rest_framework import generics

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
