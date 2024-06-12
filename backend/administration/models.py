from django.db import models

from django.core.exceptions import ValidationError


def validate_personnel_number(value):
    if len(str(value)) != 8:
        raise ValidationError("Табельный номер должен содержать ровно 8 символов и не должен начинаться с 0.")


class AdminStaff(models.Model):
    roles = [
        ("specialist", "Специалист"),
        ("operator", "Оператор")
    ]

    personnel_number = models.IntegerField(unique=True, verbose_name="Табельный номер",
                                           validators=[validate_personnel_number])
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=16, verbose_name="Телефон")
    role = models.CharField(max_length=15, choices=roles, verbose_name="Роль")
    password = models.CharField(max_length=100, verbose_name="Пароль")

    def __str__(self):
        return f"{self.personnel_number} - {self.last_name} {self.first_name}"

    class Meta:
        db_table = "admin_staff"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['-personnel_number']
