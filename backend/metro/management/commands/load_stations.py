import json
from django.core.management import BaseCommand

from metro.models import Station


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
