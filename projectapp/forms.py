from django import forms
from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):

    description = forms.Textarea()

    class Meta:
        model = Project
        fields = ['title', 'writer', 'description', 'goalamount', 'enddate', 'funding']