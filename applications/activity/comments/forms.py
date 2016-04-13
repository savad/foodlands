__author__ = 'savad'
from django import forms

from applications.activity.comments.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["object_id", "text"]
