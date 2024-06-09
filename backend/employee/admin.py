from django.contrib import admin

from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'first_name', 'second_name', 'patronymic', 'gender', 'phone', 'personnel_number', 'work_schedule')
