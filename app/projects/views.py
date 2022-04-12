from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('name', 'summarize','description', 'price', 'category', )
    template_name = 'projects/project_create_or_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ('name', 'description', 'price', 'category', )
    template_name = 'projects/project_create_or_update.html'
    success_url = reverse_lazy("projects:list")
    context_object_name = 'project'
