from django.contrib import admin

from passenger.models import Passenger, PassengerCategory


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "second_name", "patronymic", "phone", "category", "gender", "is_pacemaker", "description")


@admin.register(PassengerCategory)
class PassengerCategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "description")
