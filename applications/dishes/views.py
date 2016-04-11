__author__ = 'savad'
from django.views.generic import TemplateView


class DishListingView(TemplateView):
    """
    View for rendering Restaurant listing page
    """
    template_name = 'dishes/dish_list.html'

