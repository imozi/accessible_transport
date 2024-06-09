import json

from django.core.management import BaseCommand

from metro.models import TimeBetweenStations


class Command(BaseCommand):
    def handle(self, *args, **options):
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
