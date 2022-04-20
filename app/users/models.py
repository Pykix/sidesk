from django.contrib.auth.models import AbstractUser
from django.db import models


def get_upload_path(instance, filename):
    return f"users/{instance.project.name}/{filename}"


class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to=get_upload_path, null=True, blank=True)  # type: ignore

    def __str__(self) -> str:
        return self.username
