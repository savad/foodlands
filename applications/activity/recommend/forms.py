__author__ = 'savad'
from django import forms

from applications.activity.recommend.models import Recommend


class RecommendForm(forms.ModelForm):

    class Meta:
        model = Recommend
        fields = ["object_id"]
