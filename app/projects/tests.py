from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Category, Project


class ProjectTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            username="test01", email="test@test.fr", password="test"
        )
        category = Category.objects.create(label="Test", abbreviated="test")
        Project.objects.create(
            user=user,
            name="test",
            summarize="a resume",
            description="a desc",
            price=20000,
            category=category,
            slug="blag",
        )

    def test_project_creation(self):
        project = Project.objects.get(name="test")
        self.assertEqual(project.name, "test")
        self.assertEqual(project.slug, "test")

    def test_project_update(self):
        project = Project.objects.get(name="test")
        project.name = "new title"
        project.save()
        self.assertEqual(project.name, "new title")
        self.assertEqual(project.slug, "new-title")

    def test_project_list_view_response(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
