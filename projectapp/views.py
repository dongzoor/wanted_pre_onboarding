from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project




class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})





