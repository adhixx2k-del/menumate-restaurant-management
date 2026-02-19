import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create superuser from environment variables if one does not exist'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@menumate.com')

        if not password:
            self.stdout.write(self.style.ERROR(
                'DJANGO_SUPERUSER_PASSWORD environment variable not set. Skipping superuser creation.'
            ))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(
                f'Superuser "{username}" already exists. Skipping creation.'
            ))
        else:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )
            self.stdout.write(self.style.SUCCESS(
                f'Superuser "{username}" created successfully.'
            ))
