import random
from pathlib import Path

import factory
import factory.fuzzy
from users.models import CustomUser

from .models import Category, Project, ProjectImage


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    user = factory.Iterator(CustomUser.objects.all())
    name = factory.Faker("sentence", nb_words=2)
    summarize = factory.Faker("text", max_nb_chars=80)
    description = factory.Faker(
        "paragraph", nb_sentences=50, variable_nb_sentences=True
    )
    price = factory.Faker("random_number", digits=5, fix_len=False)
    category = factory.Iterator(Category.objects.all())
    slug = factory.Faker("company")
    visible = factory.Faker("boolean", chance_of_getting_true=100)
    ordered = factory.Faker("boolean", chance_of_getting_true=0)


class ProjectImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectImage

    project = factory.Iterator(Project.objects.all())
    image = factory.django.FileField(
        from_path="/workspace/app/static/images/computer.jpg"
    )
    alt = "Alpha presentation"
