__author__ = 'savad'
from django import forms

from applications.activity.favourite.models import Favourite


class FavouriteForm(forms.ModelForm):

    class Meta:
        model = Favourite
        fields = ["object_id"]
