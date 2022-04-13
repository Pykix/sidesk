"""core URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users.views import Login

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/', Login.as_view(), name="login"),
    path('projects/', include('projects.urls')),
    path('', include('staticpages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
