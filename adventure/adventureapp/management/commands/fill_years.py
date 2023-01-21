from django.core.management.base import BaseCommand
from adventureapp.models import MyYear
import datetime
from adventureapp.models import MyYear

class Command(BaseCommand):
    def handle(self, *args, **options):
        INIT_YEAR = 2003
        LAST_YEAR = 2022
        for y in range(INIT_YEAR, LAST_YEAR):
            dt = datetime.date(y, 1, 1)
            MyYear.objects.create(name=str(y), date=dt)
