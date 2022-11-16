import random

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand, CommandError

from api.models import Book, User, BookRecord
from library import settings


class Command(BaseCommand):
    help = "Create some data for development"

    def handle(self, *args, **options):
        if settings.DEBUG:

            books = [
                {
                    "title": "The Countess of Pembroke's Arcadia",
                    "author": "Philip Sidney",
                    "publication_year": 1593,
                },
                {
                    "title": "The Anatomy of Melancholy",
                    "author": "Robert Burton",
                    "publication_year": 1621,
                },
                {
                    "title": "Paradise Lost",
                    "author": "John Milton",
                    "publication_year": 1667,
                },
                {
                    "title": "The Starry Messenger",
                    "author": "Galileo Galilei",
                    "publication_year": 1610,
                },
            ]

            for book in books:
                Book.objects.get_or_create(
                    title=book["title"],
                    author=book["author"],
                    publication_year=book["publication_year"],
                )

            user, created = User.objects.get_or_create(username="Belletrix")
            if created:
                user.password = make_password("badpassword")
                user.save()

            for book in [Book.objects.first(), Book.objects.last()]:
                book, created = BookRecord.objects.get_or_create(
                    reader=user,
                    book=book,
                )
                if created:
                    book.reading_state = random.choice(["wr", "rg", "rd"])

            self.stdout.write(self.style.SUCCESS("Objects added to database."))

        else:
            raise CommandError("This command only runs when DEBUG is set to True.")
