from django import forms
from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):

    writer = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    description = forms.Textarea()

    class Meta:
        model = Project
        fields = ['title', 'writer', 'description', 'goalamount', 'enddate', 'funding']