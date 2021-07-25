﻿"""Forms for the blog app."""
from django import forms


class EmailPostForm(forms.Form):
    """Form for sharing a post via email."""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


