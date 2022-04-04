
from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Catégorie"

    CATEGORIES_CHOICES = (
        ('SA', 'SaaS'),
        ('ME', 'e-Commerce'),
        ('SP', 'Reseau Social'),
        ('CS', 'Relation Client'),
        ('BD', 'Big Data'),
        ('WE', 'Website / Web Application'),
        ('FT', 'Fintech'),
        ('CP', 'Crypto / Blockchain'),
        ('MA', 'Application mobile'),
        ('DA', 'Application bureau'),
    )
    label = models.CharField(choices=CATEGORIES_CHOICES, max_length=2)

    def __str__(self) -> str:
        return self.get_label_display()  # type: ignore

    def __repr__(self) -> str:
        return self.get_label_display()  # type: ignore


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField("Titre", max_length=255, unique=True)
    description = models.CharField("Description", max_length=255)
    price = models.DecimalField("Prix", max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, related_name="categories")

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title
