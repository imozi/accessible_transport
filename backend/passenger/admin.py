from django.contrib import admin

from passenger.models import Passenger, PassengerCategory, PassengerPhone


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    class PassengerPhoneInline(admin.TabularInline):
        model = PassengerPhone
        extra = 1

    list_display = (
        "first_name", "second_name", "patronymic", "category", "phones", "description", "gender", "is_pacemaker")
    inlines = [PassengerPhoneInline]

    def phones(self, obj):
        return obj.get_phones()

    phones.short_description = "Phones"


@admin.register(PassengerCategory)
class PassengerCategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "description")


@admin.register(PassengerPhone)
class PassengerPhoneAdmin(admin.ModelAdmin):
    list_display = ("number", "description", "passenger")
