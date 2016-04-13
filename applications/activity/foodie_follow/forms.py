__author__ = 'savad'
from django import forms

from applications.activity.foodie_follow.models import FoodieFollow


class FoodieFollowForm(forms.ModelForm):

    class Meta:
        model = FoodieFollow
        fields = ["following"]
