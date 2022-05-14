from django import forms

from .models import Category, Project, ProjectImage, ProjectMetric


class ProjectForm(forms.ModelForm):
    class Meta:

        category = forms.ModelChoiceField(
            queryset=Category.objects.all(), empty_label="Choisissez une catégorie"
        )
        model = Project
        fields = ("name", "summarize", "description", "price", "category", "visible")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-item"}),
            "description": forms.Textarea(attrs={"class": "bonjour"}),
            "summarize": forms.TextInput(attrs={"class": "form-item"}),
            "price": forms.NumberInput(attrs={"class": "form-item"}),
            "category": forms.Select(attrs={"class": "form-item"}),
            "visible": forms.CheckboxInput(attrs={"class": "form-item"}),
        }
        labels = {"name": "Nom du projet"}


ImageFileFormSet = forms.inlineformset_factory(
    Project,
    ProjectImage,
    fields=(
        "image",
        "alt",
    ),
    extra=1,
    can_delete_extra=False,
    form=ProjectForm,
    min_num=1,
    max_num=5,
)

MetricFormSet = forms.inlineformset_factory(
    Project,
    ProjectMetric,
    fields=("__all__"),
    extra=1,
    can_delete_extra=False,
    form=ProjectForm,
)
