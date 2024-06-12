import json
from django.core.management import BaseCommand

from metro.models import Station, TransferTime, TimeBetweenStations


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('metro/tmp/metro_stations.json', "r", encoding="utf-8") as file:
            reader_json = json.load(file)
            for station in reader_json:
                Station.objects.create(
                    id_station=station["id"],
                    name_station=station["name_station"],
                    id_line=station["id_line"],
                    name_line=station["name_line"]
                )

        with open('metro/tmp/transfer_time.json', "r", encoding="utf-8") as file:
            reader_json = json.load(file)

            for row in reader_json:
                TransferTime.objects.create(
                    id1=row["id1"],
                    id2=row["id2"],
                    time=row["time"]
                )

        with open('metro/tmp/time_between_stations.json', "r", encoding="utf-8") as file:
            reader_json = json.load(file)
            for item in reader_json:
                if "," in item["time"]:
                    item["time"] = item["time"].replace(",", ".")

            for row in reader_json:
                TimeBetweenStations.objects.create(
                    id_st1=row["id_st1"],
                    id_st2=row["id_st2"],
                    time=row["time"]
                )
