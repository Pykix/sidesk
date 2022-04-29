"""core URL Configuration
"""

from accounts.views import UserLoginFormView, UserSignUpFormView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users.views import Login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("login/", UserLoginFormView.as_view(), name="login"),
    path("signup/", UserSignUpFormView.as_view(), name="signup"),
    path("projects/", include("projects.urls")),
    path("account-settings/", include("accounts.urls")),
    path("", include("staticpages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
