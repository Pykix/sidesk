from allauth.account.forms import ChangePasswordForm
from allauth.account.views import PasswordChangeView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

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
