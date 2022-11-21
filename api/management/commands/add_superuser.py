import random

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand, CommandError

from api.models import Book, User, BookRecord
from library import settings


# To run this management command:
# python manage.py add_superuser
class Command(BaseCommand):
    help = "Create a superuser in production"

    def handle(self, *args, **options):
        if not settings.DEBUG:
          user, created = User.objects.get_or_create(
                username="admin"
            )
          if created:
            user.email = ''
            user.set_password('badpassword')
            user.is_superuser = True
            user.save()
            msg = self.style.SUCCESS(f"User 'admin' added to database.")
          else:
            msg = self.style.WARNING(f"User 'admin' already exists.")
          self.stdout.write(msg)

