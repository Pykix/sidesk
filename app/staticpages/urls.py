from django.urls import path

from .views import ContactView, LandingPage, UserCondition

urlpatterns = [
    path("", LandingPage.as_view(), name="landing-page"),
    path("cgu/", UserCondition.as_view(), name="cgu"),
    path("contact/", ContactView.as_view(), name="contact"),
]
