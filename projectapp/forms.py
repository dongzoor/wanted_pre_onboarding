from django import forms
from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):

    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    writer = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    description = forms.Textarea()

    goalamount = forms.IntegerField()

    enddate = forms.DateTimeField()

    funding = forms.IntegerField()

    class Meta:
        model = Project
        fields = ['title', 'writer', 'description', 'goalamount', 'enddate', 'funding']