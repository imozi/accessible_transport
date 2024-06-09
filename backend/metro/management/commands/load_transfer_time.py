import json

from django.core.management import BaseCommand

from metro.models import TransferTime


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('metro/tmp/transfer_time.json', "r", encoding="utf-8") as file:
            reader_json = json.load(file)

            for row in reader_json:
                TransferTime.objects.create(
                    id1=row["id1"],
                    id2=row["id2"],
                    time=row["time"]
                )
