from pathlib import Path

from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .misc import bill_number_generator


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Catégorie"

    label = models.CharField("Label", max_length=255, unique=True)
    abbreviated = models.CharField(
        "Clé", max_length=4, unique=True, help_text="4 caractère max"
    )
    color = models.CharField(max_length=7, default="#FFFFFF")

    def save(self, *args, **kwargs):
        self.abbreviated = self.abbreviated.upper()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return self.label


class Project(models.Model):
    class Meta:
        verbose_name_plural = "Projets"
        verbose_name = "Projet"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("Titre", max_length=255, unique=True)
    summarize = models.CharField(
        "Resumer", max_length=80, help_text="80 caractères max"
    )
    description = RichTextField(config_name="project_desc")
    price = models.DecimalField("Prix", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(
        null=False,
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


def get_upload_path(instance, filename):
    return f"projects/{instance.project.name}/{filename}"


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.FileField(upload_to=get_upload_path)
    alt = models.CharField("Nom de l'image", max_length=255, blank=True, null=True)

    @property
    def get_filename(self):
        path = Path(self.image.name)
        return path.stem

    def __str__(self) -> str:
        return f"{self.project.name} - {self.get_filename}"  # type: ignore


class ProjectMetric(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="metrics"
    )
    viewer_month = models.CharField(
        "Visiteur par mois",
        max_length=50,
        null=True,
        blank=True,
        default="Non communiquer",
    )
    viewer_proof = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    download_month = models.CharField(
        "Nombre de téléchargement",
        max_length=200,
        null=True,
        blank=True,
        default="Non communiquer",
    )
    download_proof = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    revenue_month = models.CharField(
        "Revenue mensuel",
        max_length=200,
        null=True,
        blank=True,
        default="Non communiquer",
    )
    revenue_proof = models.ImageField(upload_to=get_upload_path, null=True, blank=True)


class Order(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    seller = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, related_name="seller"
    )
    buyer = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, related_name="buyer"
    )
    bill_number = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.bill_number = bill_number_generator(
            self.project.name, str(self.buyer.pk), str(self.seller.pk)
        )
        self.amount = self.project.price
        self.seller = self.project.user
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.project} - {self.bill_number}"
