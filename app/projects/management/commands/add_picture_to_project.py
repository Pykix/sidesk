from django.core.management.base import BaseCommand
from projects.data_factory import ProjectImageFactory
from projects.models import Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        number_of_projects = Project.objects.all().count()
        projects_images = ProjectImageFactory.create_batch(number_of_projects)
        for project in projects_images:
            print(f"{project} - OK!")
