from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ('description', 'price', 'category', )
    template_name = 'projects/project_update.html'
    success_url = reverse_lazy("projects:list")
