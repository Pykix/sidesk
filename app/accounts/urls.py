from django.urls import path

from .views import AccountSettingsView, UserPasswordUpdateView, UserProfileUpdateView

app_name = "account_settings"

urlpatterns = [
    path("index/", AccountSettingsView.as_view(), name="index"),
    path("update/", UserProfileUpdateView.as_view(), name="update"),
    path(
        "htmx/change_password/",
        UserPasswordUpdateView.as_view(),
        name="change_password",
    ),
]
