from django.contrib import admin

from metro.models import Station, TimeBetweenStations


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name_station", "id_line", "name_line", "status")


@admin.register(TimeBetweenStations)
class TimeBetweenStationsAdmin(admin.ModelAdmin):
    list_display = ("id_st1", "id_st2", "time",)
