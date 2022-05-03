from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = "landing/landing_page.html"
    
class UserCondition(TemplateView):
    template_name = "cgu_rgpd/cgu.html"
