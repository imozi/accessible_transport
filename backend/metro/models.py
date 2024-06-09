from django.db import models


class Station(models.Model):
    status = [
        ("open", "Открыто"),
        ("close", "Закрыто")
    ]

    id_station = models.CharField(max_length=10, verbose_name="УИД станции", null=True, blank=True)
    name_station = models.CharField(max_length=100, verbose_name="Станция")
    id_line = models.CharField(max_length=10, verbose_name="УИД линии")
    name_line = models.CharField(max_length=100, verbose_name="Линия")
    status = models.CharField(max_length=10, choices=status, default="open", verbose_name="Статус")

    def __str__(self):
        return self.name_station

    class Meta:
        db_table = "metro_stations"
        verbose_name = "Станция"
        verbose_name_plural = "Станции"


class TimeBetweenStations(models.Model):
    id_st1 = models.CharField(max_length=10)
    id_st2 = models.CharField(max_length=10)
    time = models.CharField(max_length=5)

    class Meta:
        db_table = "metro_time_between_stations"
        verbose_name = "Время между станциями"
        verbose_name_plural = "Время между станциями"


class TransferTime(models.Model):
    id1 = models.CharField(max_length=10)
    id2 = models.CharField(max_length=10)
    time = models.CharField(max_length=5)

    class Meta:
        db_table = "metro_transfer_time"
        verbose_name = "Время пересадки"
