__author__ = 'savad'
from django import forms
from django.utils.translation import ugettext_lazy as _

from applications.activity.ratings.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ["object_id", "rating"]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        print rating, "ddddddddddddd"
        if rating>5:
            raise forms.ValidationError(_("Ensure this value is less than or equal to 5."))
        return rating
