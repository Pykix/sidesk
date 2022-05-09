from unicodedata import name

from django.urls import path

from .views import LandingPage, UserCondition

urlpatterns = [
    path('', LandingPage.as_view(), name='landing-page'),
    path('cgu', UserCondition.as_view(), name='cgu'),
]
