__author__ = 'savad'
from django import forms

from applications.activity.follow.models import Follow


class FollowForm(forms.ModelForm):

    class Meta:
        model = Follow
        fields = ["object_id"]
