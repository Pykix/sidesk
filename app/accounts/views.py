from allauth.account.forms import ChangePasswordForm, LoginForm, SignupForm
from allauth.account.views import LoginView, PasswordChangeView, SignupView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, View
from projects.models import Order, Project

from .forms import ProfileUserForm


class AccountSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "account_settings/index.html"


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = "account_settings/update.html"
    success_url = reverse_lazy("account_settings:index")
    form_class = ProfileUserForm

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordUpdateView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "account_settings/password_change.html"
    success_url = reverse_lazy("account_settings:index")


class UserProjectListView(ListView):
    model = Project
    template_name = "account_settings/project_list.html"
    context_object_name = "projects"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user) #type: ignore
        return queryset

class UserOrderListView(ListView):
    model = Order
    template_name = "account_settings/order_list.html"
    context_object_name = "orders"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(buyer=self.request.user) | Q(seller=self.request.user)) # type: ignore
        return queryset


class UserLoginFormView(LoginView):
    template_name = 'account/login_form.html'
    success_url = reverse_lazy("projects:list")


class UserSignUpFormView(SignupView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy("projects:list")
