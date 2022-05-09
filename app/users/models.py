from django.contrib.auth.models import AbstractUser
from django.db import models


def get_upload_path(instance, filename):
    return f"users/{instance.username}/{filename}"


class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to=get_upload_path, null=True, blank=True)

    def __str__(self) -> str:
        return self.username
