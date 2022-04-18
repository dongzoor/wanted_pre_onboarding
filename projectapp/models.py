from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=40, blank=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
    description = models.CharField(max_length=300, null=True)
    goalamount = models.IntegerField(blank=True)
    enddate = models.DateTimeField(auto_now_add=False, blank=True)
    funding = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)



