from django.db import models


class Employee(models.Model):
    genders = [
        ("male", "Мужчина"),
        ("female", "Женщина")
    ]

    work_times = [
        ("07:00-19:00", "07:00-19:00"),
        ("08:00-20:00", "08:00-20:00"),
        ("10:00-22:00", "10:00-22:00"),
        ("20:00-08:00", "20:00-08:00")
    ]

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=7, choices=genders)
    phone = models.CharField(max_length=20)
    personnel_number = models.IntegerField(unique=True, verbose_name="Табельный номер")
    work_time = models.CharField(max_length=100, choices=work_times)
    work_day = models.DateField()
    lunch_start = models.TimeField(null=True, blank=True)
    lunch_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"

    def save(self, *args, **kwargs):
        self.full_name = f"{self.second_name} {self.first_name[0]}. {self.patronymic[0]}."
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        db_table = "employee"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['full_name']
