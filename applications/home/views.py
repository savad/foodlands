__author__ = 'savad'
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    View for rendering home page
    """
    template_name = 'home/home.html'
