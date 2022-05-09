from django.core.management.base import BaseCommand
from projects.data_factory import ProjectFactory
from projects.models import Project


class Command(BaseCommand):
    help = "Create random projects"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "total", type=int, help="Number of project you want to create"
        )

    def handle(self, *args, **options):
        total = options["total"]
        projects = ProjectFactory.create_batch(int(total))
        for project in projects:
            print(project)
