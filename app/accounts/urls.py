from django.urls import path

from .views import AccountSettingsView, UserProfileUpdate

app_name = "account_settings"

urlpatterns = [
    path("index/", AccountSettingsView.as_view(), name="index"),
    path("update/", UserProfileUpdate.as_view(), name="update"),
]
