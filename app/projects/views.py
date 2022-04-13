from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import ImageFileFormSet, MetricFormSet, ProjectForm
from .models import Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    # fields = ('name', 'summarize','description', 'price', 'category', )
    template_name = 'projects/project_create_or_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['projectimage_form'] = ImageFileFormSet(
                self.request.POST, self.request.FILES, instance=self.object)
            context['projectmetric_form'] = MetricFormSet(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['projectimage_form'] = ImageFileFormSet()
            context['projectmetric_form'] = MetricFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.user = self.request.user
        projectimage_form = context['projectimage_form']
        projectmetric_form = context['projectmetric_form']
        print('je passe ici')
        if projectimage_form.is_valid() and projectmetric_form.is_valid():
            print('valid ici')

            self.object = form.save()
            projectimage_form.instance = self.object
            projectimage_form.save()
            projectmetric_form.instance = self.object
            projectmetric_form.save()

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['projectimage_form'] = ImageFileFormSet(
                self.request.POST, self.request.FILES, instance=self.object)
            context['projectmetric_form'] = MetricFormSet(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['projectimage_form'] = ImageFileFormSet(
                instance=self.object)
            context['projectmetric_form'] = MetricFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.user = self.request.user
        projectimage_form = context['projectimage_form']
        projectmetric_form = context['projectmetric_form']
        if projectimage_form.is_valid() and projectmetric_form.is_valid():
            self.object = form.save()
            projectimage_form.instance = self.object
            projectimage_form.save()
            projectmetric_form.instance = self.object
            projectmetric_form.save()

        return super().form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list')
