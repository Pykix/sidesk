"""project URL Configuration
"""


from django.urls import include, path

from .views import (ProjectCreateView, ProjectDetailView, ProjectListView,
                    ProjectUpdateView)

app_name = "projects"

urlpatterns = [
    path('', ProjectListView.as_view(), name="list"),
    path('edit/<str:slug>/', ProjectUpdateView.as_view(), name="update"),
    path('create/', ProjectCreateView.as_view(), name="create"),
    path('<str:slug>/', ProjectDetailView.as_view(), name="detail"),
]
