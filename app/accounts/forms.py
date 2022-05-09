from django import forms
from django.contrib.auth import get_user_model


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "picture",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-item"}),
            "first_name": forms.TextInput(attrs={"class": "form-item"}),
            "last_name": forms.TextInput(attrs={"class": "form-item"}),
            "picture": forms.FileInput(attrs={"class": "form-item"}),
        }
        labels = {"picture": "Photo de profil"}
