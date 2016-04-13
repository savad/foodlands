__author__ = 'savad'
from django import forms

from applications.activity.tasted.models import Tasted


class TastedForm(forms.ModelForm):

    class Meta:
        model = Tasted
        fields = ["object_id"]
