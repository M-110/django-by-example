"""Forms for the blog app."""
from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    """Form for sharing a post via email."""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Form for inputting comments for posts."""

    class Meta:
        model = Comment
        fields = 'name', 'email', 'body'



