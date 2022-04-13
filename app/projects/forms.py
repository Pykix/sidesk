

from django import forms

from .models import Project, ProjectImage


class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project
        fields = ('name', 'summarize', 'description', 'price', 'category',)
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-item'}),
            'summarize' : forms.TextInput(attrs={'class': 'form-item'}),
            'price' : forms.NumberInput(attrs={'class': 'form-item'}),
            'category' : forms.TextInput(attrs={'class': 'form-item'}),
        }
        labels = {
            'name': 'Nom du projet'
        }


ImageFileFormSet = forms.inlineformset_factory(
    Project, ProjectImage, fields=('image',), 
    can_delete_extra=False, form=ProjectForm)
