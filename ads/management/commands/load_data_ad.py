import csv

from django.core.management.base import BaseCommand

from ads.models import Ad, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('categories.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for obj in data:
                category = Category(
                    name=obj['name']
                )

                category.save()

        with open('ads.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for obj in data:
                ad = Ad(
                    name=obj['name'],
                    price=obj['price'],
                    description=obj['description'],
                    is_published=True if obj['is_published'] == 'TRUE' else False,
                    image=obj['image'],
                    author_id=obj['author_id'],
                    category_id=obj['category_id']
                )
                ad.save(

                )
