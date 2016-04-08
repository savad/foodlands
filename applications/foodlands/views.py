__author__ = 'savad'
from django.views.generic import TemplateView


class FoodlandsView(TemplateView):
    """
    View for rendering Restaurant listing page
    """
    template_name = 'foodlands/foodlands.html'

