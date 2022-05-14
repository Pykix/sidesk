from django.core.management.base import BaseCommand
from faker import Factory
from projects.data_factory import ProjectFactory
from projects.models import Category, Project


class Command(BaseCommand):

    help = "Create random projects"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "total", type=int, help="Number of project you want to create"
        )

    def handle(self, *args, **options):
        fake = Factory.create()

        WEB_APP = "WAPP"
        MOBILE_APP = "MAPP"
        SOCIAL_MEDIA = "SOME"
        CUSTOMER_RELATION = "CRM"
        BLOG = "BLOG"
        MOBILE_GAME = "MGAM"

        project_categories = [
            (WEB_APP, "Application web"),
            (MOBILE_APP, "Application mobile"),
            (SOCIAL_MEDIA, "Reseau social"),
            (CUSTOMER_RELATION, "Relation client"),
            (BLOG, "Blog"),
            (MOBILE_GAME, "Jeux mobile"),
        ]
        for index, value in enumerate(project_categories):
            cat = Category.objects.create(
                label=value[1], abbreviated=value[0], color=fake.hex_color()
            )
            print(cat)
        total = options["total"]
        projects = ProjectFactory.create_batch(int(total))
        for project in projects:
            print(project)
