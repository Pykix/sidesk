"""project URL Configuration
"""


from django.urls import path

from .views import (
    CreateOrderTemplateView,
    CreatePDFOrderView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = "projects"

urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("edit/<str:slug>/", ProjectUpdateView.as_view(), name="update"),
    path("create/", ProjectCreateView.as_view(), name="create"),
    path("delete/<str:slug>", ProjectDeleteView.as_view(), name="delete"),
    path("<str:slug>/buy/", CreateOrderTemplateView.as_view(), name="order"),
    path("<str:slug>/", ProjectDetailView.as_view(), name="detail"),
    path("order/<str:bill_number>/", CreatePDFOrderView.as_view(), name="order_pdf"),
]
