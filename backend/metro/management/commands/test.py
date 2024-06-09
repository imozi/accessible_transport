from django.core.management import BaseCommand

from metro.shortest_path import get_shortest_path


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_shortest_path("33", "439")
