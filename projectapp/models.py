from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=40)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
    description = models.CharField(max_length=300, null=True)
    goalamount = models.IntegerField()
    enddate = models.DateTimeField(auto_now_add=False)
    funding = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)



