
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import CustomUser


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Catégorie"

    label = models.CharField('Label', max_length=255, unique=True)
    abbreviated = models.CharField(
        'Clé', max_length=4, unique=True, help_text="4 caractère max")

    def save(self, *args, **kwargs):
        self.abbreviated = self.abbreviated.upper()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.abbreviated} - {self.label}"

    def __repr__(self) -> str:
        return f"{self.abbreviated} - {self.label}"


class Project(models.Model):

    class Meta:
        verbose_name_plural = "Projets"
        verbose_name = "Projet"

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField("Titre", max_length=255, unique=True)
    description = models.TextField("Description", max_length=255)
    price = models.DecimalField("Prix", max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, related_name="categories")
    slug = models.SlugField(null=False, unique=True,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
