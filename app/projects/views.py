from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
