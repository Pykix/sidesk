from re import template

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django_filters.views import FilterView

from .filters import ProjectFilter
from .forms import ImageFileFormSet, MetricFormSet, ProjectForm
from .models import Order, Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    # fields = ('name', 'summarize','description', 'price', 'category', )
    template_name = "projects/project_create_or_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["projectimage_form"] = ImageFileFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            context["projectmetric_form"] = MetricFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            context["projectimage_form"] = ImageFileFormSet()
            context["projectmetric_form"] = MetricFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.user = self.request.user
        projectimage_form = context["projectimage_form"]
        projectmetric_form = context["projectmetric_form"]
        if projectimage_form.is_valid() and projectmetric_form.is_valid():
            self.object = form.save()
            projectimage_form.instance = self.object
            projectimage_form.save()
            projectmetric_form.instance = self.object
            projectmetric_form.save()

        return super().form_valid(form)


class ProjectListView(FilterView):
    
    
    model = Project
    context_object_name = "projects"
    filterset_class = ProjectFilter
    template_name = "projects/project_list.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(visible=True)
        return queryset
    


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = (
        "name",
        "description",
        "price",
        "category",
    )
    template_name = "projects/project_create_or_update.html"
    success_url = reverse_lazy("projects:list")
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["projectimage_form"] = ImageFileFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            context["projectmetric_form"] = MetricFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            context["projectimage_form"] = ImageFileFormSet(instance=self.object)
            context["projectmetric_form"] = MetricFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.user = self.request.user
        projectimage_form = context["projectimage_form"]
        projectmetric_form = context["projectmetric_form"]
        if projectimage_form.is_valid() and projectmetric_form.is_valid():
            self.object = form.save()
            projectimage_form.instance = self.object
            projectimage_form.save()
            projectmetric_form.instance = self.object
            projectmetric_form.save()

        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin ,DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list")



class CreateOrderTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "orders/order.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(project__slug=self.kwargs['slug'])
        return context
    
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.get(slug=self.kwargs['slug'])
        
        order = Order()
        order.project = project
        order.seller = project.user # type: ignore
        order.buyer = self.request.user
        order.amount = project.price #type: ignore
        order.save()
        
        project.visible = False #type: ignore
        project.ordered = True #type: ignore
        project.save()
        
        return super().get(request, *args, **kwargs)
        
    
