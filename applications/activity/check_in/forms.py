__author__ = 'savad'
from django import forms

from applications.activity.check_in.models import CheckIn


class CheckInForm(forms.ModelForm):

    class Meta:
        model = CheckIn
        fields = ["object_id"]
