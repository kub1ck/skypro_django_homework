import csv

from django.core.management.base import BaseCommand

from user.models import Location, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('locations.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for obj in data:
                location = Location(
                    name=obj['name'],
                    lat=obj['lat'],
                    lng=obj['lng']
                )

                location.save()

        with open('users.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for obj in data:
                user = User(
                    first_name=obj['first_name'],
                    last_name=obj['last_name'],
                    username=obj['username'],
                    password=obj['password'],
                    role=obj['role'],
                    age=obj['age']
                )

                user.save()

                user.locations.add(Location.objects.get(pk=obj['id']))
                user.save()
