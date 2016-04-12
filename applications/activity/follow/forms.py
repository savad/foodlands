__author__ = 'savad'
from django import forms


class FollowForm(forms.Form):
    object_id = forms.CharField(max_length=255)
