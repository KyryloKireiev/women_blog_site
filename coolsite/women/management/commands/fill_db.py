import os

from django.core.management.base import BaseCommand
from women.models import Category, Women
from women.constants import WOMEN_CONTENT

CATEGORIES = ("Characters", "Actresses", "Models", "Writers")
WOMEN = ("Trinity", "Sarah Conor", "Angelina Jolie", "Lesya Ukrainka")
PHOTO_PATH = "coolsite/media/photos/2022/04/$d/"
PHOTO_TITLES = ("trinity.jpeg", "connor.jpeg", "angelina.jpg", "lesya.jpeg")


class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **options):
        if self.validate_fill_bd():
            return self.stdout.write(self.style.SUCCESS('Test data has already been written to the database'))

        self.create_categories()
        self.create_women()

        self.stdout.write(self.style.SUCCESS('Test data added successfully'))

    @staticmethod
    def create_categories():
        for cat in CATEGORIES:
            Category.objects.create(name=cat)

    @staticmethod
    def create_women():
        for index, woman in enumerate(WOMEN):
            photo_filename = os.path.basename(f"{PHOTO_PATH}{PHOTO_TITLES[index]}")
            obj = Women.objects.create(
                title=WOMEN[index],
                content=WOMEN_CONTENT[woman],
                cat=Category.objects.get(pk=index + 1)
            )
            obj.photo.save(photo_filename, open(f"{PHOTO_PATH}{PHOTO_TITLES[index]}", "rb"), save=True)

    @staticmethod
    def validate_fill_bd():
        return Category.objects.filter(name__in=CATEGORIES).exists()

