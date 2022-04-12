
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    name = models.CharField("Titre", max_length=255, unique=True)
    summarize = models.CharField(
        "Résumer", max_length=80, help_text="80 caractères max")
    description = RichTextField(config_name='project_desc')
    price = models.DecimalField("Prix", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
