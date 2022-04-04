"""core URL Configuration
"""

from django.contrib import admin
from django.urls import include, path
from users.views import Login

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', Login.as_view(), name="login"),
    path('projects/', include('projects.urls')),
]
