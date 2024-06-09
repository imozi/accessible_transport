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
    category = models.ForeignKey(PassengerCategory, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=7, choices=genders)
    is_pacemaker = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.second_name} {self.first_name} - {self.category.code}"

    def get_phones(self):
        return ", ".join([f"{phone.number} ({phone.description})" for phone in self.phones.all()])

    class Meta:
        db_table = "passenger"
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"
        ordering = ['second_name']


class PassengerPhone(models.Model):
    number = models.CharField(max_length=15)
    description = models.CharField(max_length=250, blank=True, null=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return f"{self.number}"

    class Meta:
        db_table = "passenger_phone"
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"
