import datetime

from django.db import models

from employee.models import Employee
from metro.models import Station
from metro.shortest_path import get_shortest_path
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
    status = models.ForeignKey(RequestStatus, on_delete=models.SET_NULL, null=True, default=14)
    description = models.CharField(max_length=500, null=True, blank=True)
    from_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name='route_from')
    to_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name='route_to')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='requests')

    def save(self, *args, **kwargs):
        if self.passenger and not self.category:
            self.category = self.passenger.category
        t = get_shortest_path(self.from_station.id_station, self.to_station.id_station)

        hours = t // 60
        minutes = t % 60

        t1 = self.time_start
        if t < 10:
            t2 = datetime.timedelta(hours=hours, minutes=minutes + 5)
        elif 10 < t < 20:
            t2 = datetime.timedelta(hours=hours, minutes=minutes + 10)
        elif 20 < t < 30:
            t2 = datetime.timedelta(hours=hours, minutes=minutes + 15)
        else:
            t2 = datetime.timedelta(hours=hours, minutes=minutes + 30)

        res = datetime.datetime.combine(datetime.date.min, t1) + t2
        self.time_end = res.time()
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.status} / {self.passenger} / {self.date}: {self.time_start} - {self.time_end}"

    class Meta:
        db_table = "request"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-date']
