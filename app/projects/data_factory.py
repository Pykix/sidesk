import random

import factory
import factory.fuzzy
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from users.models import CustomUser

from .models import Category, Project, ProjectImage


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    user = factory.Iterator(CustomUser.objects.all())
    name = factory.Faker("company")
    summarize = factory.Faker("text", max_nb_chars=80)
    description = factory.Faker(
        "paragraph", nb_sentences=50, variable_nb_sentences=True
    )
    price = factory.Faker("random_number", digits=5, fix_len=False)
    category = factory.Iterator(Category.objects.all())
    slug = factory.Faker("company")
    visible = factory.Faker("boolean", chance_of_getting_true=100)
    ordered = factory.Faker("boolean", chance_of_getting_true=0)


class CategoryFactory(factory.django.DjangoModelFactory):
    WEB_APP = "WAPP"
    MOBILE_APP = "MAPP"
    SOCIAL_MEDIA = "SOME"
    CUSTOMER_RELATION = "CRM"
    BLOG = "BLOG"
    MOBILE_GAME = "MGAM"

    PROJECT_CATEGORIES = [
        (WEB_APP, "Application web"),
        (MOBILE_APP, "Application mobile"),
        (SOCIAL_MEDIA, "Reseau social"),
        (CUSTOMER_RELATION, "Relation client"),
        (BLOG, "Blog"),
        (MOBILE_GAME, "Jeux mobile"),
    ]
    random_categories = random.choices(PROJECT_CATEGORIES)

    class Meta:
        model = Category


# class ProjectImageFactory(factory.django.DjangoModelFactory):
#     project = factory.Iterator(Project.objects.all())
#     image = factory.django.FileField(from_path="/static/images/computer.jpg")
#     alt = "Alpha presentation"
