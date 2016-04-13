__author__ = 'savad'
from django import forms
from django.utils.translation import ugettext_lazy as _

from applications.activity.review.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["object_id", "review_text", "food_rating",
                  "ambiance_rating", "service_rating"]

    def clean_food_rating(self):
        review_text = self.cleaned_data["review_text"]
        food_rating = self.cleaned_data["food_rating"]
        if review_text and not food_rating:
            raise forms.ValidationError(_("This field is required."))
        if food_rating>5 or food_rating<1:
            raise forms.ValidationError(_("Invalid data."))
        return food_rating

    def clean_ambiance_rating(self):
        review_text = self.cleaned_data["review_text"]
        ambiance_rating = self.cleaned_data["ambiance_rating"]
        if review_text and not ambiance_rating:
            raise forms.ValidationError(_("This field is required."))
        if ambiance_rating>5 or ambiance_rating<1:
            raise forms.ValidationError(_("Invalid data."))
        return ambiance_rating

    def clean_service_rating(self):
        review_text = self.cleaned_data["review_text"]
        service_rating = self.cleaned_data["service_rating"]
        if review_text and not service_rating:
            raise forms.ValidationError(_("This field is required."))
        if service_rating>5 or service_rating<1:
            raise forms.ValidationError(_("Invalid data."))
        return service_rating
