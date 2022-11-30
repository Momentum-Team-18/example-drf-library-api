import random

from django.core.management.base import BaseCommand

from api.models import User
from library import settings


# To run this management command:
# python manage.py add_superuser
class Command(BaseCommand):
    help = "Create a superuser in production"

    def handle(self, *args, **options):
        if not settings.DEBUG:
          user, created = User.objects.get_or_create(
                username=settings.DJANGO_SUPERUSER_USERNAME
            )
          if created:
            user.email = ''
            user.set_password(settings.DJANGO_SUPERUSER_PASSWORD)
            user.is_superuser = True
            user.save()
            msg = self.style.SUCCESS(f"Superuser {settings.DJANGO_SUPERUSER_USERNAME} added to database.")
          else:
            msg = self.style.WARNING(f"Superuser {settings.DJANGO_SUPERUSER_USERNAME} already exists.")
          self.stdout.write(msg)

