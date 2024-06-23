from rest_framework import serializers

from employee.models import Employee
from requests.models import Request


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RequestEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'date', 'time_start', 'time_end')


class EmployeeDetailRequestsSerializer(serializers.ModelSerializer):
    requests = RequestEmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'full_name', "work_time", "work_day", "lunch_start", "lunch_end", 'requests')
