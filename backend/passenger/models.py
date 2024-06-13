from django.db import models


class PassengerCategory(models.Model):
    code = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.description}"

    class Meta:
        db_table = "passenger_category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['code']


class Passenger(models.Model):
    genders = [
        ("male", "Мужчина"),
        ("female", "Женщина")
    ]

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    category = models.ForeignKey(PassengerCategory, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=7, choices=genders)
    is_pacemaker = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.second_name} {self.first_name}"

    class Meta:
        db_table = "passenger"
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"
        ordering = ['-pk']
