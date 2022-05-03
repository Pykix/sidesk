from django.core.management.base import BaseCommand
from users.data_factory import UsersFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = UsersFactory.create_batch(10)
        for user in users:
            print(user)
    