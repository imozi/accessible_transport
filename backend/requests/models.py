from django.db import models

from employee.models import Employee
from metro.models import Station
from passenger.models import Passenger, PassengerCategory


class RequestStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        db_table = "request_status"
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статус заявок"


class Request(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='requests')
    category = models.ForeignKey(PassengerCategory, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(RequestStatus, on_delete=models.SET_NULL, null=True, default=1)
    description = models.CharField(max_length=500, null=True, blank=True)
    from_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name='route_from')
    to_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name='route_to')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField(null=True, blank=True)
    employee = models.ManyToManyField(Employee, blank=True, related_name='requests')
    employees_number = models.IntegerField(default=1, null=True, blank=True)

    def get_related_objects(self):
        # возвращает ограниченное количество связанных объектов
        return '\n'.join([str(obj) for obj in self.employee.all()[:5]])

    get_related_objects.short_description = 'Employees'

    def save(self, *args, **kwargs):
        cancel_statuses = ["Отмена", "Отказ"]
        if self.status.status in cancel_statuses:
            self.employee.clear()
        if self.passenger and not self.category:
            self.category = self.passenger.category
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.status} / {self.passenger} / {self.date}: {self.time_start} - {self.time_end}"

    class Meta:
        db_table = "request"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-date']
