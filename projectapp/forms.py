from django import forms
from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'goalamount', 'enddate', 'funding']
