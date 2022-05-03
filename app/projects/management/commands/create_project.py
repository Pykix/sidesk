from django.core.management.base import BaseCommand
from projects.data_factory import ProjectFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        projects = ProjectFactory.create_batch(10)
        for project in projects:
            print(project)
    