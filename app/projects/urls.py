"""project URL Configuration
"""

from unicodedata import name

from django.urls import include, path

from .views import ProjectListView

app_name = "projects"

urlpatterns = [
    path('', ProjectListView.as_view(), name="list")
]
