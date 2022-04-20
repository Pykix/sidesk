from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView


class AccountSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "account_settings/index.html"


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = settings.AUTH_USER_MODEL
    fields = (
        "username",
        "first_name",
        "last_name",
    )
    template_name = "account_settings/update.html"
