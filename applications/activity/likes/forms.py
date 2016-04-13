__author__ = 'savad'
from django import forms

from applications.activity.likes.models import Like


class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = ["object_id"]
